import cv2
import numpy as np
import winsound
import pyttsx3
import yagmail

cap = cv2.VideoCapture(0)
_, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

engine = pyttsx3.init()

yag = yagmail.SMTP("Emailadresin@gmail.com", "Emailşifren")
to = "Göndereceğinemail@gmail.com"
mail_count = 0

while True:
    _, curr_frame = cap.read()
    curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prev_gray, curr_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])

    avg_magnitude = np.mean(magnitude)
    if avg_magnitude > 5:
        winsound.Beep(2500, 500)
        print("deprem oluyor!")

        engine.setProperty('rate', 200)
        engine.say("Deprem oluyor")
        engine.runAndWait()

        yag.send(to=to, subject="Deprem Oluyor!", contents="Deprem Oluyor! Lütfen güvenli bir yere gidin.")
        mail_count += 1

    prev_gray = curr_gray
    cv2.putText(curr_frame, "Titresim Buyuklugu: {:.2f}".format(avg_magnitude), (7, 60), cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (0, 0, 255), 2)
    cv2.putText(curr_frame, "Gonderilen Mail Sayisi: {}".format(mail_count), (7, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                (255, 255, 255), 2)


    cv2.imshow("Kamera", curr_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()