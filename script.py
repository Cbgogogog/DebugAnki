# coding: utf-8
#
import uiautomator2 as u2
import time

d = u2.connect()

d(text="AnkiDroid").click()

d(resourceId="com.ichi2.anki.debug:id/sync_profile").click()

d.xpath('//*[@resource-id="com.ichi2.anki.debug:id/MyAccountLayout"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]').click()
d.click(0.073, 0.772)
d.xpath('//*[@resource-id="com.ichi2.anki.debug:id/password_layout"]/android.widget.FrameLayout[1]').click()
d.click(0.069, 0.77)
d(resourceId="com.ichi2.anki.debug:id/login_button").click()