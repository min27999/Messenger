import socket
from PyQt5.QtCore import QThread, pyqtSignal

class Client(QThread):
    def __init__(self, window, nickname, channel):
        super().__init__(window)
        self.server = "125.240.245.248"
        self.port = 1234
        self.nickname = nickname
        self.channel = '#' + channel

    chattingChanged = pyqtSignal(str)

    def get_response(self):
        return self.conn.recv(512).decode("utf-8")

    def send_cmd(self, cmd, message):
        command = "{} {}\r\n".format(cmd, message).encode("utf-8")
        self.conn.send(command)

    def send_message_to_channel(self, message):
        command = "PRIVMSG {}".format(self.channel)
        message = ":" + message
        self.send_cmd(command, message)

    def join_channel(self):
        cmd = "JOIN"
        channel = self.channel
        self.send_cmd(cmd, channel)

    def run(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.server, self.port))
        joined = False
        cmd = ''

        while(joined == False):
            resp = self.get_response()
            print(resp.strip())
            if "No Ident response" in resp:
                self.send_cmd("NICK", self.nickname)
                self.send_cmd(
                    "USER", "{} * * :{}".format(self.nickname, self.nickname))

            # we're accepted, now let's join the channel!
            if "376" in resp:
                self.join_channel()

            # username already in use? try to use username with _
            if "433" in resp:
                username = "_" + username
                self.send_cmd("NICK", username)
                self.send_cmd(
                    "USER", "{} * * :{}".format(username, username))

            # if PING send PONG with name of the server
            if "PING" in resp:
                self.send_cmd("PONG", ":" + resp.split(":")[1])

            # we've joined
            if "366" in resp:
                joined = True

        while True:
            resp = self.get_response()
            if resp:
                msg = resp.strip().split(":")
                msg = "<{}> {}".format(msg[1].split("!")[0], msg[-1].strip())
                self.chattingChanged.emit(msg)
