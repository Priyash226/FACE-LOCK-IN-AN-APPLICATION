import socket
import time
import threading
from tkinter import *
import os
 
 
def main_program():
    root=Tk()
    root.geometry("300x500")
    root.config(bg="white")
 
    def func():
        t=threading.Thread(target=recv)
        t.start()
 
 
    def recv():
        listensocket=socket.socket()
        port=3050
        maxconnection=99
        ip=socket.gethostname()
        print(ip)
 
        listensocket.bind(('',port))
        listensocket.listen(maxconnection)
        (clientsocket,address)=listensocket.accept()
         
        while True:
            sendermessage=clientsocket.recv(1024).decode()
            if not sendermessage=="":
                time.sleep(5)
                lstbx.insert(0,"Client : "+sendermessage)
 
 
    s=0
 
    def sendmsg():
        global s
        if s==0:
            s=socket.socket()
            hostname=''
            port=4050
            s.connect((hostname,port))
            msg=messagebox.get()
            lstbx.insert(0,"You : "+msg)
            s.send(msg.encode())
        else:
            msg=messagebox.get()
            lstbx.insert(0,"You : "+msg)
            s.send(msg.encode())
 
 
    def threadsendmsg():
        th=threading.Thread(target=sendmsg)
        th.start()
 
 
 
 
    startchatimage=PhotoImage(file='start.png')
 
    buttons=Button(root,image=startchatimage,command=func,borderwidth=0)
    buttons.place(x=90,y=10)
 
    message=StringVar()
    messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=32)
    messagebox.place(x=10,y=444)
 
    sendmessageimg=PhotoImage(file='send.png')
 
    sendmessagebutton=Button(root,image=sendmessageimg,command=threadsendmsg,borderwidth=0)
    sendmessagebutton.place(x=260,y=440)
 
    lstbx=Listbox(root,height=20,width=43)
    lstbx.place(x=15,y=80)
 
    user_name = Label(root,text =" Number" ,width=10)
 
    root.mainloop()
    os._exit(1)
 
 
 
 
 
import face_recognition
import cv2
import numpy as np
 
video = cv2.VideoCapture(0)
 
face = face_recognition.load_image_file("1.jpg")
faceencoding = face_recognition.face_encodings(face)[0]
 
face_encodings_list = [
    faceencoding]
 
face_encodings = []
s = True
face_coordinates=[]
 
 
while True:
    _,frame = video.read()
 
    resized_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
 
    resized_frame_rgb = resized_frame[:, :, ::-1]
 
 
    if s:
        face_coordinates = face_recognition.face_locations(resized_frame_rgb)
        face_encodings = face_recognition.face_encodings(resized_frame_rgb, face_coordinates)
 
        for faces in face_encodings:
            matches = face_recognition.compare_faces(face_encodings_list, faces)
            if matches[0] == True:
                video.release()
                cv2.destroyAllWindows()
                main_program()
    cv2.imshow('Face Scan', frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
video.release()
cv2.destroyAllWindows()
