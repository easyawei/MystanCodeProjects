"""
File: my_drawing.py
Name: chaowei hsieh
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon
from campy.graphics.gwindow import GWindow

window = GWindow(width=800, height=600, title="I am a Baikinman")


def main():
    """
    Title: 細菌人, assignment maker。

    在每週四新的assignment發佈前, 都會想著不知道這回細菌人會帶怎樣新難題給各位麵包超人。
    """

    face()
    eyes()
    mouth()
    teeth()
    nose()
    antenna()
    white_paper()

    # reference line
    # line_ub = GLine(x0=400, y0=0, x1=400, y1=600)
    # line_lr = GLine(x0=0, y0=300, x1=800, y1=300)
    # line_nose = GLine(x0=0, y0=370, x1=800, y1=370)
    # line_antenna = GLine(x0=0, y0=90, x1=800, y1=90)
    # window.add(line_ub)
    # window.add(line_lr)
    # window.add(line_nose)
    # window.add(line_antenna)


def face():
    size_face = 400
    size_face2 = 800

    # face (main big face)
    face_m = GOval(size_face, size_face, x=(window.width-size_face)/2, y=(window.height-size_face)*3/4)
    face_m.filled = True
    face_m.fill_color = (53, 66, 75)
    window.add(face_m)

    # face_l (left)
    face_l = GOval(size_face2, size_face2, x=-160, y=350)
    face_l.filled = True
    face_l.fill_color = (118, 111, 178)
    window.add(face_l)

    # face_r (right)
    face_r = GOval(size_face2, size_face2, x=160, y=350)
    face_r.filled = True
    face_r.fill_color = (118, 111, 178)
    window.add(face_r)


def eyes():
    size_eyes = 40
    size_eyes2 = 70

    # eyes (left), outside
    eye_l2 = GOval(size_eyes2, size_eyes2, x=(window.width-size_eyes2*3)/2, y=(window.height-size_eyes2)/2)
    eye_l2.filled = True
    eye_l2.fill_color = (251, 212, 219)
    window.add(eye_l2)

    # eyes (left), inside, black
    eye_l = GOval(size_eyes*0.8, size_eyes*0.8, x=(window.width-size_eyes*3.5)/2, y=(window.height-size_eyes*0.7)/2)
    eye_l.filled = True
    eye_l.fill_color = (0, 0, 0)
    window.add(eye_l)

    # eyes (right), outside
    eye_r2 = GOval(size_eyes2, size_eyes2, x=(window.width+size_eyes2*1)/2, y=(window.height-size_eyes2)/2)
    eye_r2.filled = True
    eye_r2.fill_color = (251, 212, 219)
    window.add(eye_r2)

    # eyes (right), inside, black
    eye_r = GOval(size_eyes*0.8, size_eyes*0.8, x=(window.width+size_eyes*2)/2, y=(window.height-size_eyes*0.7)/2)
    eye_r.filled = True
    eye_r.fill_color = (0, 0, 0)
    window.add(eye_r)


def mouth():
    size_face = 400
    size_mouth = 800

    # mouth (upper)
    mouth_m = GOval(size_mouth, size_mouth, x=(window.width-size_mouth)/2, y=395)
    mouth_m.filled = True
    mouth_m.fill_color = (255, 255, 255)
    window.add(mouth_m)

    # mouth (bottom)
    face_mouth = GOval(size_face, size_face, x=(window.width-size_face)/2, y=(window.height-size_face)*3/4)
    window.add(face_mouth)


def teeth():

    # teeth (centre line)
    teeth_c = GLine(400, 395, 400, 550)
    window.add(teeth_c)

    # teeth (right side)
    teeth_r1 = GLine(460, 400, 460, 540)
    teeth_r2 = GLine(520, 413, 520, 510)
    window.add(teeth_r1)
    window.add(teeth_r2)

    # teeth (left side)
    teeth_l1 = GLine(340, 400, 340, 540)
    teeth_l2 = GLine(280, 413, 280, 510)
    window.add(teeth_l1)
    window.add(teeth_l2)

    # teeth (lines go down, separate up and bottom)
    teeth_d01 = GLine(240, 430, 285, 480)
    teeth_d02 = GLine(320, 450, 355, 485)
    teeth_d03 = GLine(390, 460, 415, 485)
    teeth_d04 = GLine(445, 460, 485, 480)
    teeth_d05 = GLine(510, 455, 530, 465)
    window.add(teeth_d01)
    window.add(teeth_d02)
    window.add(teeth_d03)
    window.add(teeth_d04)
    window.add(teeth_d05)

    # teeth (lines go up, separate up and bottom)
    teeth_u01 = GLine(285, 480, 320, 450)
    teeth_u02 = GLine(355, 485, 390, 460)
    teeth_u03 = GLine(415, 485, 445, 460)
    teeth_u04 = GLine(485, 480, 510, 455)
    teeth_u05 = GLine(530, 465, 580, 437)
    window.add(teeth_u01)
    window.add(teeth_u02)
    window.add(teeth_u03)
    window.add(teeth_u04)
    window.add(teeth_u05)


def nose():
    size_nose = 110
    size_nose2 = 25

    # nose, circle, purple
    nose_m = GOval(size_nose, size_nose, x=(window.width-size_nose)/2, y=335)
    nose_m.filled = True
    nose_m.fill_color = (118, 111, 178)
    window.add(nose_m)

    # nose, rectangle, white
    nose2 = GRect(size_nose2, size_nose2, x=(window.width-size_nose2)/2, y=360)
    nose2.filled = True
    nose2.fill_color = (255, 255, 255)
    nose2.color = (255, 255, 255)
    window.add(nose2)


def antenna():
    size_antenna = 60

    # antenna (left)
    triangle_l = GPolygon()
    triangle_l.add_vertex((280, 190))
    triangle_l.add_vertex((320, 167))
    triangle_l.add_vertex((250, 90))
    triangle_l.filled = True
    triangle_l.fill_color = (53, 66, 75)
    window.add(triangle_l)

    antenna_left = GOval(size_antenna, size_antenna, x=(window.width-size_antenna*5.9)/2, y=60)
    antenna_left.filled = True
    antenna_left.fill_color = (53, 66, 75)
    window.add(antenna_left)

    # antenna (right)
    triangle_r = GPolygon()
    triangle_r.add_vertex((520, 190))
    triangle_r.add_vertex((480, 167))
    triangle_r.add_vertex((560, 90))
    triangle_r.filled = True
    triangle_r.fill_color = (53, 66, 75)
    window.add(triangle_r)

    antenna_right = GOval(size_antenna, size_antenna, x=(window.width+size_antenna*4.3)/2, y=60)
    antenna_right.filled = True
    antenna_right.fill_color = (53, 66, 75)
    window.add(antenna_right)


def white_paper():

    # white paper (left, face repair, 01p01)
    triangle_01p1 = GPolygon()
    triangle_01p1.add_vertex((200, 457))
    triangle_01p1.add_vertex((219, 438))
    triangle_01p1.add_vertex((194, 380))
    triangle_01p1.filled = True
    triangle_01p1.fill_color = (255, 255, 255)
    triangle_01p1.color = (255, 255, 255)
    window.add(triangle_01p1)

    # withe paper (left, face repair, 01p02)
    triangle_01p2 = GPolygon()
    triangle_01p2.add_vertex((190, 417))
    triangle_01p2.add_vertex((207, 410))
    triangle_01p2.add_vertex((198, 370))
    triangle_01p2.filled = True
    triangle_01p2.fill_color = (255, 255, 255)
    triangle_01p2.color = (255, 255, 255)
    window.add(triangle_01p2)

    # withe paper (left)
    paper_01 = GRect(199, 600, x=0, y=0)
    paper_01.filled = True
    paper_01.fill_color = (255, 255, 255)
    paper_01.color = (255, 255, 255)
    window.add(paper_01)

    # white paper (right, face repair, 02p1)
    triangle_02p1 = GPolygon()
    triangle_02p1.add_vertex((580, 440))
    triangle_02p1.add_vertex((605, 457))
    triangle_02p1.add_vertex((607, 380))
    triangle_02p1.filled = True
    triangle_02p1.fill_color = (255, 255, 255)
    triangle_02p1.color = (255, 255, 255)
    window.add(triangle_02p1)

    # white paper (right, face repair, 02p2)
    triangle_02p2 = GPolygon()
    triangle_02p2.add_vertex((590, 420))
    triangle_02p2.add_vertex((600, 420))
    triangle_02p2.add_vertex((607, 360))
    triangle_02p2.filled = True
    triangle_02p2.fill_color = (255, 255, 255)
    triangle_02p2.color = (255, 255, 255)
    window.add(triangle_02p2)

    # white paper (right, face repair, 02p3)
    triangle_02p3 = GPolygon()
    triangle_02p3.add_vertex((595, 410))
    triangle_02p3.add_vertex((620, 380))
    triangle_02p3.add_vertex((603, 360))
    triangle_02p3.filled = True
    triangle_02p3.fill_color = (255, 255, 255)
    triangle_02p3.color = (255, 255, 255)
    window.add(triangle_02p3)

    # withe paper (right)
    paper_02 = GRect(200, 600, x=601, y=0)
    paper_02.filled = True
    paper_02.fill_color = (255, 255, 255)
    paper_02.color = (255, 255, 255)
    window.add(paper_02)


if __name__ == '__main__':
    main()
