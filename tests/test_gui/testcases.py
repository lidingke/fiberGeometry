# coding:utf-8
import os
import pdb
from time import sleep
import logging
logger = logging.getLogger(__name__)
# from util.unittest.demogui import View
# from util.unittest.gui import View

def knife_into_demo(view_instance, app):
    # sleep()
    from util.unittest.knife import Knife

    knife = Knife(view_instance)
    # print dir(knife)
    view_instance.input_line.setText("123")
    knife.enter_button.clicked()
    sleep(1)
    text = view_instance.output_line.text()
    assert text == "122"
    sleep(1)
    view_instance.input_line.setText("1234")
    sleep(1)
    knife.enter_button.clicked()
    text = view_instance.output_line.text()
    assert text == "1233"
    sleep(3)
    view_instance.close()
    # os._exit(0)


def knife_into_cv(view_instance, app):
    from util.unittest.knife import Knife

    knife = Knife(view_instance)
    sleep(1)
    knife._view.beginTestCV.clicked()
    text0 = view_instance._view.resultShowCV.toPlainText()
    tick = 0
    while True:
        sleep(0.1)
        text = view_instance._view.resultShowCV.toPlainText()
        tick = tick+1
        if text != text0:
            break
        if tick > 100:
            logger.error("thread time out")
            break

    print unicode(text)
    assert unicode(text).find(u"芯包同心度") > 0
    sleep(0.1)
    # app.quit()
    view_instance.close()



def knife_into_cap(view_instance, app):
    from util.unittest.knife import Knife

    knife = Knife(view_instance)
    sleep(0.1)
    # print dir(knife._view)
    # view_instance.input_line.setText("123")
    knife._view.beginTestCV.clicked()

    # sleep(10)

    text0 = view_instance._view.resultShowCV.toPlainText()
    tick = 0
    while True:
        sleep(0.1)
        text = view_instance._view.resultShowCV.toPlainText()
        tick = tick+1
        if text != text0:
            break
        if tick > 100:
            logger.error("thread time out")
            break

    print unicode(text)
    assert unicode(text).find(u"芯包同心度") > 0

    sleep(0.1)
    # app.quit()
    view_instance.close()


# def test_knife_into_main(view_instance):
#     knife = Knife(view_instance)
#     knife.view.target_button.clicked()
#     sleep(10)
#     text = view_instance._view.show_plain.toPlainText()
#     assert unicode(text) == "target"
