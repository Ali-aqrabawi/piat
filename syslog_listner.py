from piat.listeners.syslog_listener import run


def syslog_cb(syslog_msg):
    msg_dict = syslog_msg.get_dictionary()

    print(msg_dict)
    print("###################")


run([syslog_cb])
