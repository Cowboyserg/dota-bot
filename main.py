import ctypes
import time
import pyautogui
from PIL import ImageGrab, ImageOps

SendInput = ctypes.windll.user32.SendInput

time.sleep(3)
def which_lvl():
    screen = ImageGrab.grab()
    obj = screen.load()
    screen = ImageGrab.grab()
    obj = screen.load()
    if obj[596, 1050] == (0, 0, 0) and obj[597, 1050] == (0, 0, 0) and obj[598, 1050] == (0, 0, 0) and obj[
        599, 1050] == (0, 0, 0) and obj[600, 1050] == (1, 0, 0) and obj[601, 1050] == (3, 1, 0) and obj[602, 1050] == (
    12, 2, 0) and obj[603, 1050] == (27, 8, 0) and obj[604, 1050] == (45, 17, 1) and obj[605, 1050] == (65, 28, 1) and \
            obj[606, 1050] == (87, 41, 2) and obj[607, 1050] == (178, 159, 109) and obj[608, 1050] == (168, 144, 96) and \
            obj[609, 1050] == (146, 100, 55) and obj[610, 1050] == (182, 165, 113) and obj[611, 1050] == (
    172, 149, 100) and obj[612, 1050] == (113, 54, 3) and obj[613, 1050] == (90, 42, 2) and obj[614, 1050] == (
    66, 29, 1) and obj[615, 1050] == (43, 16, 1) and obj[616, 1050] == (22, 6, 0):
        return ("лвл 1")
    elif obj[596, 1050] == (0, 0, 0) and obj[597, 1050] == (0, 0, 0) and obj[598, 1050] == (0, 0, 0) and obj[
        599, 1050] == (0, 0, 0) and obj[600, 1050] == (3, 1, 0) and obj[601, 1050] == (10, 2, 0) and obj[602, 1050] == (
    25, 7, 0) and obj[603, 1050] == (41, 16, 1) and obj[604, 1050] == (60, 25, 1) and obj[605, 1050] == (77, 35, 1) and \
            obj[606, 1050] == (154, 132, 88) and obj[607, 1050] == (152, 127, 83) and obj[608, 1050] == (114, 55, 3) and \
            obj[609, 1050] == (120, 58, 4) and obj[610, 1050] == (127, 62, 4) and obj[611, 1050] == (134, 71, 19) and \
            obj[612, 1050] == (179, 161, 109) and obj[613, 1050] == (181, 164, 112) and obj[614, 1050] == (
    108, 51, 2) and obj[615, 1050] == (87, 40, 2) and obj[616, 1050] == (63, 27, 1):
        return ("лвл 2")
    elif obj[596, 1050] == (0, 0, 0) and obj[597, 1050] == (0, 0, 0) and obj[598, 1050] == (0, 0, 0) and obj[
        599, 1050] == (0, 0, 0) and obj[600, 1050] == (1, 0, 0) and obj[601, 1050] == (5, 1, 0) and obj[602, 1050] == (
    16, 4, 0) and obj[603, 1050] == (30, 9, 0) and obj[604, 1050] == (47, 19, 1) and obj[605, 1050] == (65, 28, 1) and \
            obj[606, 1050] == (101, 69, 37) and obj[607, 1050] == (109, 65, 29) and obj[608, 1050] == (114, 55, 3) and \
            obj[609, 1050] == (125, 60, 4) and obj[610, 1050] == (132, 64, 4) and obj[611, 1050] == (171, 147, 98) and \
            obj[612, 1050] == (182, 165, 113) and obj[613, 1050] == (129, 89, 50) and obj[614, 1050] == (93, 43, 2) and \
            obj[615, 1050] == (70, 31, 1) and obj[616, 1050] == (47, 19, 1):
        return ("лвл 3")
    elif obj[596, 1050] == (0, 0, 0) and obj[597, 1050] == (0, 0, 0) and obj[598, 1050] == (0, 0, 0) and obj[
        599, 1050] == (0, 0, 0) and obj[600, 1050] == (0, 0, 0) and obj[601, 1050] == (1, 0, 0) and obj[602, 1050] == (
    2, 1, 0) and obj[603, 1050] == (9, 2, 0) and obj[604, 1050] == (25, 7, 0) and obj[605, 1050] == (45, 17, 1) and obj[
        606, 1050] == (66, 29, 1) and obj[607, 1050] == (89, 41, 2) and obj[608, 1050] == (108, 52, 3) and obj[
        609, 1050] == (130, 75, 31) and obj[610, 1050] == (181, 163, 112) and obj[611, 1050] == (182, 165, 113) and obj[
        612, 1050] == (175, 154, 104) and obj[613, 1050] == (115, 55, 3) and obj[614, 1050] == (93, 43, 2) and obj[
        615, 1050] == (68, 30, 1) and obj[616, 1050] == (44, 17, 1):
        return ("лвл 4")
    elif obj[596, 1050] == (0, 0, 0) and obj[597, 1050] == (0, 0, 0) and obj[598, 1050] == (0, 0, 0) and obj[
        599, 1050] == (0, 0, 0) and obj[600, 1050] == (1, 0, 0) and obj[601, 1050] == (5, 1, 0) and obj[602, 1050] == (
    20, 5, 0) and obj[603, 1050] == (40, 15, 1) and obj[604, 1050] == (62, 27, 1) and obj[605, 1050] == (86, 40, 2) and \
            obj[606, 1050] == (109, 52, 3) and obj[607, 1050] == (162, 136, 90) and obj[608, 1050] == (
    182, 165, 113) and obj[609, 1050] == (136, 68, 11) and obj[610, 1050] == (129, 63, 4) and obj[611, 1050] == (
    119, 58, 4) and obj[612, 1050] == (107, 51, 3) and obj[613, 1050] == (90, 43, 2) and obj[614, 1050] == (
    72, 32, 1) and obj[615, 1050] == (52, 21, 1) and obj[616, 1050] == (34, 11, 0):
        return ("лвл 5")
    elif obj[596, 1050] == (0, 0, 0) and obj[597, 1050] == (0, 0, 0) and obj[598, 1050] == (0, 0, 0) and obj[
        599, 1050] == (0, 0, 0) and obj[600, 1050] == (1, 0, 0) and obj[601, 1050] == (3, 1, 0) and obj[602, 1050] == (
    12, 3, 0) and obj[603, 1050] == (29, 9, 0) and obj[604, 1050] == (50, 21, 1) and obj[605, 1050] == (73, 33, 1) and \
            obj[606, 1050] == (96, 45, 2) and obj[607, 1050] == (114, 54, 3) and obj[608, 1050] == (157, 128, 82) and \
            obj[609, 1050] == (182, 165, 113) and obj[610, 1050] == (156, 125, 80) and obj[611, 1050] == (
    117, 56, 3) and obj[612, 1050] == (102, 48, 2) and obj[613, 1050] == (83, 38, 2) and obj[614, 1050] == (
    60, 26, 1) and obj[615, 1050] == (39, 15, 1) and obj[616, 1050] == (20, 5, 0):
        return ("лвл 6")
    elif obj[596, 1050] == (0, 0, 0) and obj[597, 1050] == (0, 0, 0) and obj[598, 1050] == (0, 0, 0) and obj[
        599, 1050] == (0, 0, 0) and obj[600, 1050] == (2, 1, 0) and obj[601, 1050] == (8, 2, 0) and obj[602, 1050] == (
    21, 5, 0) and obj[603, 1050] == (36, 12, 0) and obj[604, 1050] == (53, 22, 1) and obj[605, 1050] == (72, 33, 1) and \
            obj[606, 1050] == (90, 41, 2) and obj[607, 1050] == (104, 49, 2) and obj[608, 1050] == (117, 56, 3) and obj[
        609, 1050] == (128, 62, 4) and obj[610, 1050] == (135, 67, 5) and obj[611, 1050] == (165, 134, 87) and obj[
        612, 1050] == (182, 165, 113) and obj[613, 1050] == (135, 94, 52) and obj[614, 1050] == (100, 47, 2) and obj[
        615, 1050] == (77, 35, 1) and obj[616, 1050] == (53, 22, 1):
        return ("лвл 7")
    elif obj[596, 1050] == (0, 0, 0) and obj[597, 1050] == (0, 0, 0) and obj[598, 1050] == (0, 0, 0) and obj[
        599, 1050] == (1, 0, 0) and obj[600, 1050] == (4, 1, 0) and obj[601, 1050] == (16, 4, 0) and obj[602, 1050] == (
    34, 12, 1) and obj[603, 1050] == (56, 24, 1) and obj[604, 1050] == (79, 36, 1) and obj[605, 1050] == (
    101, 48, 2) and obj[606, 1050] == (159, 133, 87) and obj[607, 1050] == (183, 166, 114) and obj[608, 1050] == (
    152, 106, 61) and obj[609, 1050] == (139, 68, 4) and obj[610, 1050] == (139, 68, 5) and obj[611, 1050] == (
    147, 98, 52) and obj[612, 1050] == (182, 165, 113) and obj[613, 1050] == (165, 142, 94) and obj[614, 1050] == (
    102, 49, 2) and obj[615, 1050] == (81, 37, 1) and obj[616, 1050] == (58, 25, 1):
        return ("лвл 8")
    elif obj[596, 1050] == (0, 0, 0) and obj[597, 1050] == (0, 0, 0) and obj[598, 1050] == (0, 0, 0) and obj[
        599, 1050] == (2, 0, 0) and obj[600, 1050] == (9, 2, 0) and obj[601, 1050] == (24, 7, 0) and obj[602, 1050] == (
    44, 17, 1) and obj[603, 1050] == (66, 29, 1) and obj[604, 1050] == (89, 41, 2) and obj[605, 1050] == (
    110, 53, 5) and obj[606, 1050] == (181, 163, 112) and obj[607, 1050] == (175, 155, 105) and obj[608, 1050] == (
    131, 64, 4) and obj[609, 1050] == (129, 63, 4) and obj[610, 1050] == (130, 63, 4) and obj[611, 1050] == (
    134, 71, 21) and obj[612, 1050] == (181, 163, 111) and obj[613, 1050] == (177, 158, 108) and obj[614, 1050] == (
    109, 52, 2) and obj[615, 1050] == (87, 40, 2) and obj[616, 1050] == (64, 28, 1):
        return ("лвл 9")
    elif obj[596, 1050] == (3, 1, 0) and obj[597, 1050] == (12, 2, 0) and obj[598, 1050] == (28, 8, 0) and obj[
        599, 1050] == (46, 18, 1) and obj[600, 1050] == (66, 29, 1) and obj[601, 1050] == (88, 41, 2) and obj[
        602, 1050] == (178, 159, 109) and obj[603, 1050] == (168, 145, 97) and obj[604, 1050] == (146, 100, 56) and obj[
        605, 1050] == (183, 166, 114) and obj[606, 1050] == (173, 150, 101) and obj[607, 1050] == (118, 56, 4) and obj[
        608, 1050] == (105, 49, 3) and obj[609, 1050] == (101, 48, 2) and obj[610, 1050] == (110, 52, 3) and obj[
        611, 1050] == (142, 103, 61) and obj[612, 1050] == (182, 165, 113) and obj[613, 1050] == (161, 131, 84) and obj[
        614, 1050] == (131, 64, 4) and obj[615, 1050] == (131, 64, 4) and obj[616, 1050] == (151, 112, 67):
        return ("лвл 10")
    elif obj[596, 1050] == (3, 1, 0) and obj[597, 1050] == (12, 2, 0) and obj[598, 1050] == (28, 8, 0) and obj[
        599, 1050] == (46, 18, 1) and obj[600, 1050] == (66, 29, 1) and obj[601, 1050] == (88, 41, 2) and obj[
        602, 1050] == (178, 159, 109) and obj[603, 1050] == (168, 145, 97) and obj[604, 1050] == (146, 100, 56) and obj[
        605, 1050] == (183, 166, 114) and obj[606, 1050] == (173, 150, 101) and obj[607, 1050] == (114, 55, 3) and obj[
        608, 1050] == (95, 45, 2) and obj[609, 1050] == (80, 36, 1) and obj[610, 1050] == (79, 36, 1) and obj[
        611, 1050] == (90, 42, 2) and obj[612, 1050] == (177, 158, 108) and obj[613, 1050] == (167, 144, 96) and obj[
        614, 1050] == (145, 99, 55) and obj[615, 1050] == (182, 165, 113) and obj[616, 1050] == (171, 149, 100):
        return ("лвл 11")
    elif obj[596, 1050] == (3, 1, 0) and obj[597, 1050] == (12, 2, 0) and obj[598, 1050] == (28, 8, 0) and obj[
        599, 1050] == (46, 18, 1) and obj[600, 1050] == (66, 29, 1) and obj[601, 1050] == (88, 41, 2) and obj[
        602, 1050] == (178, 159, 109) and obj[603, 1050] == (168, 145, 97) and obj[604, 1050] == (146, 100, 56) and obj[
        605, 1050] == (183, 166, 114) and obj[606, 1050] == (173, 150, 101) and obj[607, 1050] == (116, 56, 4) and obj[
        608, 1050] == (100, 47, 2) and obj[609, 1050] == (88, 41, 2) and obj[610, 1050] == (88, 41, 2) and obj[
        611, 1050] == (153, 132, 87) and obj[612, 1050] == (151, 126, 83) and obj[613, 1050] == (114, 55, 3) and obj[
        614, 1050] == (120, 58, 4) and obj[615, 1050] == (126, 62, 4) and obj[616, 1050] == (133, 70, 19):
        return ("лвл 12")
    elif obj[596, 1050] == (3, 1, 0) and obj[597, 1050] == (12, 2, 0) and obj[598, 1050] == (28, 8, 0) and obj[
        599, 1050] == (46, 18, 1) and obj[600, 1050] == (66, 29, 1) and obj[601, 1050] == (88, 41, 2) and obj[
        602, 1050] == (178, 159, 109) and obj[603, 1050] == (168, 145, 97) and obj[604, 1050] == (146, 100, 56) and obj[
        605, 1050] == (183, 166, 114) and obj[606, 1050] == (173, 150, 101) and obj[607, 1050] == (115, 55, 3) and obj[
        608, 1050] == (96, 45, 2) and obj[609, 1050] == (81, 37, 2) and obj[610, 1050] == (78, 36, 1) and obj[
        611, 1050] == (103, 70, 37) and obj[612, 1050] == (109, 65, 29) and obj[613, 1050] == (114, 55, 3) and obj[
        614, 1050] == (125, 60, 4) and obj[615, 1050] == (132, 64, 4) and obj[616, 1050] == (171, 147, 98):
        return ("лвл 13")
    elif obj[596, 1050] == (3, 1, 0) and obj[597, 1050] == (12, 2, 0) and obj[598, 1050] == (28, 8, 0) and obj[
        599, 1050] == (46, 18, 1) and obj[600, 1050] == (66, 29, 1) and obj[601, 1050] == (88, 41, 2) and obj[
        602, 1050] == (178, 159, 109) and obj[603, 1050] == (168, 145, 97) and obj[604, 1050] == (146, 100, 56) and obj[
        605, 1050] == (183, 166, 114) and obj[606, 1050] == (173, 150, 101) and obj[607, 1050] == (114, 54, 3) and obj[
        608, 1050] == (92, 43, 2) and obj[609, 1050] == (71, 32, 1) and obj[610, 1050] == (63, 28, 1) and obj[
        611, 1050] == (71, 32, 1) and obj[612, 1050] == (89, 42, 2) and obj[613, 1050] == (108, 51, 3) and obj[
        614, 1050] == (129, 74, 31) and obj[615, 1050] == (181, 163, 111) and obj[616, 1050] == (181, 164, 113):
        return ("лвл 14")
    elif obj[596, 1050] == (3, 1, 0) and obj[597, 1050] == (12, 2, 0) and obj[598, 1050] == (28, 8, 0) and obj[
        599, 1050] == (46, 18, 1) and obj[600, 1050] == (66, 29, 1) and obj[601, 1050] == (88, 41, 2) and obj[
        602, 1050] == (178, 159, 109) and obj[603, 1050] == (168, 145, 97) and obj[604, 1050] == (146, 100, 56) and obj[
        605, 1050] == (183, 166, 114) and obj[606, 1050] == (173, 150, 101) and obj[607, 1050] == (116, 55, 4) and obj[
        608, 1050] == (99, 47, 2) and obj[609, 1050] == (90, 42, 2) and obj[610, 1050] == (95, 45, 2) and obj[
        611, 1050] == (110, 53, 3) and obj[612, 1050] == (162, 135, 89) and obj[613, 1050] == (182, 165, 113) and obj[
        614, 1050] == (135, 67, 11) and obj[615, 1050] == (129, 63, 4) and obj[616, 1050] == (119, 58, 4):
        return ("лвл 15")
    elif obj[596, 1050] == (3, 1, 0) and obj[597, 1050] == (12, 2, 0) and obj[598, 1050] == (28, 8, 0) and obj[
        599, 1050] == (46, 18, 1) and obj[600, 1050] == (66, 29, 1) and obj[601, 1050] == (88, 41, 2) and obj[
        602, 1050] == (178, 159, 109) and obj[603, 1050] == (168, 145, 97) and obj[604, 1050] == (146, 100, 56) and obj[
        605, 1050] == (183, 166, 114) and obj[606, 1050] == (173, 150, 101) and obj[607, 1050] == (114, 55, 4) and obj[
        608, 1050] == (96, 45, 2) and obj[609, 1050] == (83, 38, 2) and obj[610, 1050] == (85, 39, 2) and obj[
        611, 1050] == (98, 46, 2) and obj[612, 1050] == (113, 54, 3) and obj[613, 1050] == (157, 127, 82) and obj[
        614, 1050] == (181, 164, 113) and obj[615, 1050] == (156, 125, 80) and obj[616, 1050] == (117, 56, 3):
        return ("лвл 16")
    elif obj[596, 1050] == (3, 1, 0) and obj[597, 1050] == (12, 2, 0) and obj[598, 1050] == (28, 8, 0) and obj[
        599, 1050] == (46, 18, 1) and obj[600, 1050] == (66, 29, 1) and obj[601, 1050] == (88, 41, 2) and obj[
        602, 1050] == (178, 159, 109) and obj[603, 1050] == (168, 145, 97) and obj[604, 1050] == (146, 100, 56) and obj[
        605, 1050] == (183, 166, 114) and obj[606, 1050] == (173, 150, 101) and obj[607, 1050] == (115, 56, 3) and obj[
        608, 1050] == (97, 46, 2) and obj[609, 1050] == (84, 39, 2) and obj[610, 1050] == (84, 39, 2) and obj[
        611, 1050] == (92, 43, 2) and obj[612, 1050] == (104, 49, 2) and obj[613, 1050] == (116, 55, 3) and obj[
        614, 1050] == (127, 62, 4) and obj[615, 1050] == (135, 67, 5) and obj[616, 1050] == (164, 134, 86):
        return ("лвл 17")
    elif obj[596, 1050] == (3, 1, 0) and obj[597, 1050] == (12, 2, 0) and obj[598, 1050] == (28, 8, 0) and obj[
        599, 1050] == (46, 18, 1) and obj[600, 1050] == (66, 29, 1) and obj[601, 1050] == (88, 41, 2) and obj[
        602, 1050] == (178, 159, 109) and obj[603, 1050] == (168, 145, 97) and obj[604, 1050] == (146, 100, 56) and obj[
        605, 1050] == (183, 166, 114) and obj[606, 1050] == (173, 150, 101) and obj[607, 1050] == (118, 56, 4) and obj[
        608, 1050] == (105, 50, 3) and obj[609, 1050] == (100, 48, 2) and obj[610, 1050] == (108, 52, 3) and obj[
        611, 1050] == (159, 132, 87) and obj[612, 1050] == (182, 165, 113) and obj[613, 1050] == (151, 106, 61) and obj[
        614, 1050] == (138, 67, 4) and obj[615, 1050] == (138, 67, 5) and obj[616, 1050] == (147, 98, 52):
        return ("лвл 18")
    elif obj[596, 1050] == (3, 1, 0) and obj[597, 1050] == (12, 2, 0) and obj[598, 1050] == (28, 8, 0) and obj[
        599, 1050] == (46, 18, 1) and obj[600, 1050] == (66, 29, 1) and obj[601, 1050] == (88, 41, 2) and obj[
        602, 1050] == (178, 159, 109) and obj[603, 1050] == (168, 145, 97) and obj[604, 1050] == (146, 100, 56) and obj[
        605, 1050] == (183, 166, 114) and obj[606, 1050] == (173, 150, 101) and obj[607, 1050] == (121, 58, 4) and obj[
        608, 1050] == (109, 53, 3) and obj[609, 1050] == (108, 52, 3) and obj[610, 1050] == (116, 56, 5) and obj[
        611, 1050] == (180, 163, 111) and obj[612, 1050] == (174, 154, 104) and obj[613, 1050] == (130, 63, 4) and obj[
        614, 1050] == (129, 63, 4) and obj[615, 1050] == (129, 63, 4) and obj[616, 1050] == (133, 71, 21):
        return ("лвл 19")
    elif obj[596, 1050] == (10, 2, 0) and obj[597, 1050] == (25, 7, 0) and obj[598, 1050] == (42, 16, 1) and obj[
        599, 1050] == (61, 26, 1) and obj[600, 1050] == (78, 36, 1) and obj[601, 1050] == (155, 133, 88) and obj[
        602, 1050] == (152, 127, 83) and obj[603, 1050] == (114, 55, 3) and obj[604, 1050] == (121, 58, 4) and obj[
        605, 1050] == (127, 62, 4) and obj[606, 1050] == (135, 71, 19) and obj[607, 1050] == (180, 162, 110) and obj[
        608, 1050] == (182, 164, 113) and obj[609, 1050] == (128, 63, 4) and obj[610, 1050] == (127, 62, 4) and obj[
        611, 1050] == (146, 105, 62) and obj[612, 1050] == (182, 165, 113) and obj[613, 1050] == (161, 131, 84) and obj[
        614, 1050] == (132, 64, 4) and obj[615, 1050] == (131, 64, 4) and obj[616, 1050] == (151, 112, 67):
        return ("лвл 20")
    elif obj[596, 1050] == (10, 2, 0) and obj[597, 1050] == (25, 7, 0) and obj[598, 1050] == (42, 16, 1) and obj[
        599, 1050] == (61, 26, 1) and obj[600, 1050] == (78, 36, 1) and obj[601, 1050] == (155, 133, 88) and obj[
        602, 1050] == (152, 127, 83) and obj[603, 1050] == (114, 55, 3) and obj[604, 1050] == (121, 58, 4) and obj[
        605, 1050] == (127, 62, 4) and obj[606, 1050] == (135, 71, 19) and obj[607, 1050] == (180, 162, 110) and obj[
        608, 1050] == (182, 164, 113) and obj[609, 1050] == (116, 55, 3) and obj[610, 1050] == (107, 51, 2) and obj[
        611, 1050] == (106, 50, 2) and obj[612, 1050] == (177, 159, 108) and obj[613, 1050] == (167, 144, 96) and obj[
        614, 1050] == (145, 99, 55) and obj[615, 1050] == (182, 165, 113) and obj[616, 1050] == (171, 149, 100):
        return ("лвл 21")
    elif obj[596, 1050] == (10, 2, 0) and obj[597, 1050] == (25, 7, 0) and obj[598, 1050] == (42, 16, 1) and obj[
        599, 1050] == (61, 26, 1) and obj[600, 1050] == (78, 36, 1) and obj[601, 1050] == (155, 133, 88) and obj[
        602, 1050] == (152, 127, 83) and obj[603, 1050] == (114, 55, 3) and obj[604, 1050] == (121, 58, 4) and obj[
        605, 1050] == (127, 62, 4) and obj[606, 1050] == (135, 71, 19) and obj[607, 1050] == (180, 162, 110) and obj[
        608, 1050] == (182, 164, 113) and obj[609, 1050] == (120, 58, 4) and obj[610, 1050] == (112, 54, 3) and obj[
        611, 1050] == (157, 133, 87) and obj[612, 1050] == (153, 127, 83) and obj[613, 1050] == (116, 55, 3) and obj[
        614, 1050] == (121, 58, 4) and obj[615, 1050] == (126, 62, 4) and obj[616, 1050] == (133, 70, 19):
        return ("лвл 22")
    elif obj[596, 1050] == (10, 2, 0) and obj[597, 1050] == (25, 7, 0) and obj[598, 1050] == (42, 16, 1) and obj[
        599, 1050] == (61, 26, 1) and obj[600, 1050] == (78, 36, 1) and obj[601, 1050] == (155, 133, 88) and obj[
        602, 1050] == (152, 127, 83) and obj[603, 1050] == (114, 55, 3) and obj[604, 1050] == (121, 58, 4) and obj[
        605, 1050] == (127, 62, 4) and obj[606, 1050] == (135, 71, 19) and obj[607, 1050] == (180, 162, 110) and obj[
        608, 1050] == (182, 164, 113) and obj[609, 1050] == (116, 55, 3) and obj[610, 1050] == (106, 51, 2) and obj[
        611, 1050] == (116, 74, 37) and obj[612, 1050] == (115, 68, 29) and obj[613, 1050] == (116, 56, 3) and obj[
        614, 1050] == (125, 61, 4) and obj[615, 1050] == (132, 64, 4) and obj[616, 1050] == (171, 147, 98):
        return ("лвл 23")
    elif obj[596, 1050] == (10, 2, 0) and obj[597, 1050] == (25, 7, 0) and obj[598, 1050] == (42, 16, 1) and obj[
        599, 1050] == (61, 26, 1) and obj[600, 1050] == (78, 36, 1) and obj[601, 1050] == (155, 133, 88) and obj[
        602, 1050] == (152, 127, 83) and obj[603, 1050] == (114, 55, 3) and obj[604, 1050] == (121, 58, 4) and obj[
        605, 1050] == (127, 62, 4) and obj[606, 1050] == (135, 71, 19) and obj[607, 1050] == (180, 162, 110) and obj[
        608, 1050] == (182, 164, 113) and obj[609, 1050] == (112, 53, 3) and obj[610, 1050] == (97, 45, 2) and obj[
        611, 1050] == (90, 43, 2) and obj[612, 1050] == (97, 46, 2) and obj[613, 1050] == (110, 53, 3) and obj[
        614, 1050] == (129, 74, 31) and obj[615, 1050] == (181, 163, 111) and obj[616, 1050] == (181, 164, 113):
        return ("лвл 24")
    elif obj[596, 1050] == (10, 2, 0) and obj[597, 1050] == (25, 7, 0) and obj[598, 1050] == (42, 16, 1) and obj[
        599, 1050] == (61, 26, 1) and obj[600, 1050] == (78, 36, 1) and obj[601, 1050] == (155, 133, 88) and obj[
        602, 1050] == (152, 127, 83) and obj[603, 1050] == (114, 55, 3) and obj[604, 1050] == (121, 58, 4) and obj[
        605, 1050] == (127, 62, 4) and obj[606, 1050] == (135, 71, 19) and obj[607, 1050] == (180, 162, 110) and obj[
        608, 1050] == (182, 164, 113) and obj[609, 1050] == (122, 59, 4) and obj[610, 1050] == (118, 57, 4) and obj[
        611, 1050] == (122, 59, 4) and obj[612, 1050] == (163, 136, 89) and obj[613, 1050] == (182, 165, 113) and obj[
        614, 1050] == (135, 68, 11) and obj[615, 1050] == (129, 63, 4) and obj[616, 1050] == (119, 58, 4):
        return ("лвл 25")
    else:
        return ("БЕЗ ЛВЛА")



class Coor_r:
    one = (96, 1026)
    two = (116, 1013)
    three = (126, 990)
    four = (129, 1033)
    five = (170, 1032)
    six = (196, 1028)

class Coor_d:
    one = (55, 903)
    two = (81, 885)
    three = (92, 890)
    four = (110, 925)
    five = (119, 904)
    six = (145, 906)

class active:
    attack = 0x04
    shift = 0x2A
    ctrl = 0x1D
    bye = 0x2F
    deliver = 0x22
    e = 0x12
    q = 0x10
    w = 0x11
    space = 0x39
    calcel = 0x03
    esc = 0x01
    hero = (671, 971)
    play = (1583, 1021)
    turbo = (1555, 733)
    tren = (1648, 277)
    talant = (804, 918)
    talant1 = (881, 873)
    talant2 = (889, 823)
    talant3 = (885, 765)
    talant4 = (887, 712)
    skill1 = (872, 920)
    skill2 = (939, 920)
    skill3 = (1002, 921)
    skill4 = (1065, 918)
    secret_d = (197, 982)
    secret_r = (47, 938)
    spisok = (122, 24)
class Heroes:
    axe = (294, 201)
    wk = (972, 302)
    troll = (704, 499)
    seeker = (306, 420)
    tide = (612, 320)
class items:
    shop = (1698, 1045)
    shield = (1755, 195)
    qb = (1759, 228)
    boot = (1816, 298)
    mask = (1822, 519)
    best = (1832, 113)
    vlad = (1680, 487)
    heart = (1784, 635)
heroes = [Heroes.axe, Heroes.wk, Heroes.troll, Heroes.seeker, Heroes.tide]
# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

def press(x):
    PressKey(x)
    time.sleep(0.2)
    ReleaseKey(x)
start_all = time.clock()
metka = 0

#Попытка отследить, где мы во время запуска
while True:

    while True:
        start = 0
        ensh = 0
        out = 0
        metka = 0
        metka1 = 0
        metka2 = 0
        metka3 = 0
        side = 0
        flag = 0
        flag1 = 0
        can = 0
        taras = 0
        side = 0
        if flag == 1:
            flag = 0
        screen = ImageGrab.grab()
        obj = screen.load()
        for i in range(974, 988):
            for j in range(793, 914):
                if obj[i,j] == (79, 95, 103):
                    pyautogui.click(962, 807)
                    flag = 1
                    continue
        if obj[1583, 1021] == (80, 88, 88) and obj[1584, 1021] == (80, 88, 88) and obj[1585, 1021] == (81, 89, 89):
            print("Можем отправляться")
            time.sleep(1)
            pyautogui.click(active.play)
            time.sleep(0.5)
            pyautogui.click(active.tren)
            time.sleep(0.5)
            screen = ImageGrab.grab()
            obj = screen.load()
            break
        elif obj[1397,814 ] ==  (81, 98, 106):
            pyautogui.click(1397, 814)
            print("Ваша порядочность")
            continue
        elif obj[ 1002 , 622 ] ==  (81, 98, 106):#Вышло обновление
            time.sleep(1)
            press(active.esc)
            pyautogui.click(1907, 24)
            time.sleep(5)
            pyautogui.click(886, 598)
            time.sleep(5)
            pyautogui.click(1752, 1059)
            time.sleep(5)
            pyautogui.click(1712, 942,button='right')
            time.sleep(5)
            pyautogui.click(1747, 739)
            time.sleep(5)
            pyautogui.click(926, 618)
            continue
        elif (obj[1685, 1048] == (184, 128, 0) and obj[1686, 1048] == (184, 128, 0)) or  (obj[ 1675 , 1047 ] ==  (71, 77, 82)):
            pyautogui.click(active.spisok)
            time.sleep(0.5)
            screen = ImageGrab.grab()
            obj = screen.load()
            for i in range(171, 341):
                if side == "radiant" or side == "dire":
                    break
                for j in range(98, 351):
                    if obj[i, j] == (255, 255, 255):
                        side = "radiant"
                        print(side)
                        press(active.esc)
                        break
            if side != "radiant":
                side = "dire"
                print(side)
                press(active.esc)
            print("Начинаем в бою")
            print(side)
            start = "fight"
            break

        elif obj[989, 623] ==  (81, 97, 105):
            print("Требуется обновлелие, нажимаем ок")
            pyautogui.click( 989 , 623 )#Требуется обновление
            press(active.esc)
            exit(0)
            continue
        elif obj[ 1506 , 879 ] ==  (81, 97, 105):
            pyautogui.click(1506, 879)#Кнопка ок в порядочности
            continue
        else:
            print("Не понятно что происходит")
            press(active.esc)
            continue

    if start != "fight":
        if obj[1713, 327] !=  (224, 238, 240):
            print(1)
            metka1 = 1
            pyautogui.click(1713, 327)
            metka1 = 0
            time.sleep(1)
        if obj[1556, 516] != (224, 238, 240):
            print(2)
            metka2 = 1
            pyautogui.click(1555, 517)
            metka2 = 0
            time.sleep(1)
        if obj[1714, 544 ] !=  (215, 229, 234):
            print(3)
            metka3 = 1
            pyautogui.click(1713, 545)
            metka3 = 0
            time.sleep(1)
        pyautogui.click(1703, 411)
        time.sleep(0.5)
        pyautogui.click(1662, 455)
        time.sleep(0.5)
        pyautogui.click(active.play)
        time.sleep(0.5)
        while True:
            screen = ImageGrab.grab()
            obj = screen.load()
            if obj[1049, 521] == (58, 93, 77):
                print("Принимаем игру")
                pyautogui.click(1049, 521)
                time.sleep(1)
                press(active.esc)
                continue
            elif obj[271, 1037] == (16, 199, 33):
                side = "radiant"
                break
            elif obj[360, 881] == (9, 185, 21):
                side = "dire"
                break
            elif obj[1583, 1021] == (80, 88, 88) and obj[1584, 1021] == (80, 88, 88) and obj[1585, 1021] == (81, 89, 89):
                print("Кто - то вылетел, заново")
                out = 1
                continue
            else:
                time.sleep(1)
                continue
        for i in heroes:
            pyautogui.click(i)
            time.sleep(0.5)
            screen = ImageGrab.grab()
            obj = screen.load()
            if obj[1527, 792] != (36, 37, 38):
                pyautogui.click(1527, 792)
                break
            else:
                continue
        while True:
            screen = ImageGrab.grab()
            obj = screen.load()
            if obj[1685, 1048] == (184, 128, 0) and obj[1686, 1048] == (184, 128, 0):
                break
            else:
                time.sleep(5)
                continue
        start_time = time.clock()
        pyautogui.click(items.shop)
        time.sleep(0.5)
        pyautogui.click(items.shield, button='right')
        time.sleep(0.5)
        pyautogui.click(items.qb, button='right')

        PressKey(active.ctrl)
        PressKey(active.shift)
        pyautogui.click(items.boot)
        time.sleep(0.5)
        ReleaseKey(active.ctrl)
        ReleaseKey(active.shift)

        pyautogui.click(items.best)
        time.sleep(0.5)
        PressKey(active.ctrl)
        PressKey(active.shift)
        pyautogui.click(items.heart)
        pyautogui.click(items.vlad)
        time.sleep(0.5)
        ReleaseKey(active.ctrl)
        ReleaseKey(active.shift)
        press(active.esc)
        time.sleep(120)

    #side = "radiant"
    start_time = time.clock()
    print(side)
    if start == "fight" or start != "fight":
        if side == "radiant":
            while True:
                if flag1 == 1:
                    break
                screen = ImageGrab.grab()
                obj = screen.load()
                if obj[1583, 1021] == (80, 88, 88) and obj[1584, 1021] == (80, 88, 88) and obj[1585, 1021] == (81, 89, 89):
                    print("Во время игры кто - то вылетел, заново", time.clock()-start_time)
                    break
                elif obj[1692, 870] == (142, 163, 201):
                    print("Забираем предметы из тайника")
                    pyautogui.click(1692, 870)

                # проверка тараски
                if taras == 0:
                    pyautogui.click(items.shop)
                    pyautogui.click(items.best)

                    screen = ImageGrab.grab()
                    obj = screen.load()
                # тараска
                if obj[1765, 630] == (205, 150, 7) and taras == 0:
                    print("Попали сюда?")
                    while True:
                        pyautogui.click(active.secret_r, button='right')
                        screen = ImageGrab.grab()
                        obj = screen.load()
                        if obj[1677, 1044] == (165, 112, 0):
                            print("Попали и сюда")
                            press(active.esc)
                            time.sleep(1)
                            pyautogui.click(items.shop)
                            time.sleep(1)
                            pyautogui.click(1757, 587)
                            time.sleep(1)
                            pyautogui.click(1679, 799, button='right')
                            time.sleep(1)
                            press(active.esc)
                            taras = 1
                            break
                        elif obj[1583, 1021] == (80, 88, 88) and obj[1584, 1021] == (80, 88, 88) and obj[1585, 1021] == (81, 89, 89):
                            out = 1
                        break
                else:
                    press(active.esc)
                if out == 1:
                    break
                elif obj[1891, 1049] == (135, 159, 204):
                    print("Никто не вызывает куру, мы ее вызываем", time.clock()-start_time)
                    press(active.deliver)
                else:
                    PressKey(active.shift)
                    press(active.deliver)
                    ReleaseKey(active.shift)

                if which_lvl() == "лвл 1":
                    print("лвл 1")
                    pyautogui.click(active.skill3)
                if which_lvl() == "лвл 2":
                    print("лвл 2")
                    pyautogui.click(active.skill1)
                if which_lvl() == "лвл 3":
                    print("лвл 3")
                    pyautogui.click(active.skill3)
                if which_lvl() == "лвл 4":
                    print("лвл 4")
                    pyautogui.click(active.skill1)
                if which_lvl() == "лвл 5":
                    print("лвл 5")
                    pyautogui.click(active.skill3)
                if which_lvl() == "лвл 6":
                    print("лвл 6")
                    pyautogui.click(active.skill1)
                if which_lvl() == "лвл 7":
                    print("лвл 7")
                    pyautogui.click(active.skill3)
                if which_lvl() == "лвл 8":
                    print("лвл 8")
                    pyautogui.click(active.skill1)
                if which_lvl() == "лвл 9":
                    print("лвл 9")
                    pyautogui.click(active.skill2)
                if which_lvl() == "лвл 10":
                    print("лвл 10")
                    pyautogui.click(active.talant)
                    pyautogui.click(active.talant1)
                if which_lvl() == "лвл 11":
                    print("лвл 11")
                    pyautogui.click(active.skill2)
                if which_lvl() == "лвл 12":
                    print("лвл 12")
                    pyautogui.click(active.skill2)
                if which_lvl() == "лвл 13":
                    print("лвл 13")
                    pyautogui.click(active.skill2)
                if which_lvl() == "лвл 15":
                    print("лвл 15")
                    pyautogui.click(active.talant)
                    pyautogui.click(active.talant2)
                if which_lvl() == "лвл 20":
                    print("лвл 20")
                    pyautogui.click(active.talant)
                    pyautogui.click(active.talant3)
                if which_lvl() == "лвл 25":
                    print("лвл 25")
                    pyautogui.click(active.talant)
                    pyautogui.click(active.talant4)

                PressKey(active.shift)
                pyautogui.moveTo(Coor_r.one)
                press(active.attack)

                screen = ImageGrab.grab()
                obj = screen.load()

                while obj[ 1002 , 921 ] ==  (98, 66, 5):
                    screen = ImageGrab.grab()
                    obj = screen.load()
                    pyautogui.click(active.skill3)
                    time.sleep(0.3)
                    print("Прокачали 3 талант")
                while obj[ 872 , 920 ] ==  (100, 68, 5):
                    screen = ImageGrab.grab()
                    obj = screen.load()
                    pyautogui.click(active.skill1)
                    time.sleep(0.3)
                    print("Прокачали 1 талант")
                while obj[ 939 , 920 ] ==  (100, 67, 5):
                    screen = ImageGrab.grab()
                    obj = screen.load()
                    pyautogui.click(active.skill2)
                    time.sleep(0.3)
                    print("Прокачали 2 талант")
                while obj[ 1065 , 918 ] ==  (99, 66, 5):
                    screen = ImageGrab.grab()
                    obj = screen.load()
                    pyautogui.click(active.skill4)
                    time.sleep(0.3)
                    print("Прокачали 4 талант")

                screen = ImageGrab.grab()
                obj = screen.load()
                if can != 1:
                    if obj[601, 1053] == (64, 27, 1) and obj[602, 1053] == (87, 40, 2) and  obj[603, 1053] == (110, 52, 3) and obj[604, 1053] == (128, 61, 4) and obj[605, 1053] == (191, 173, 119) and obj[606, 1053] == (180, 157, 105) and obj[607, 1053] == (128, 62, 4) and obj[608, 1053] == (118, 57, 3) and obj[609, 1053] == (118, 58, 3) and obj[610, 1053] == (132, 75, 28) and obj[611, 1053] == (190, 172, 118) and obj[612, 1053] == (177, 152, 101) and obj[613, 1053] == (129, 63, 4) and obj[614, 1053] == (120, 58, 4) and obj[615, 1053] == (119, 57, 4) and obj[616, 1053] == (127, 61, 4) and obj[617, 1053] == (164, 133, 86) and obj[618, 1053] == (189, 171, 117) and obj[619, 1053] == (146, 106, 63) and obj[620, 1053] == (104, 49, 3):
                        if obj[ 1142 , 957 ] ==  (148, 147, 117) or obj[ 1207 , 959 ] ==  (164, 162, 133) or obj[ 1268 , 956 ] ==  (158, 157, 127) or obj[ 1140 , 1004 ] ==  (186, 186, 160) or obj[ 1206 , 1004 ] ==  (183, 184, 156) or obj[ 1271 , 1003 ] ==  (163, 163, 134):
                            print("10 лвл и vlad, можем идти на эншетов", time.clock()-start_time)
                            ensh = 1
                            can = 1

                pyautogui.moveTo(Coor_r.two)
                press(active.attack)
                if can == 1:
                    ReleaseKey(active.shift)
                    pyautogui.moveTo(Coor_r.three)
                    press(active.attack)
                    PressKey(active.shift)
                    can = 0
                if ensh == 1:
                    PressKey(active.shift)
                    pyautogui.moveTo(Coor_r.three)
                    press(active.attack)
                pyautogui.moveTo(Coor_r.four)
                press(active.attack)
                pyautogui.moveTo(Coor_r.five)
                press(active.attack)
                pyautogui.moveTo(Coor_r.six)
                press(active.attack)
                ReleaseKey(active.shift)

                press(active.bye)
                time.sleep(0.5)
                press(active.bye)
                time.sleep(0.5)
                press(active.bye)
                time.sleep(0.5)
                press(active.bye)
                time.sleep(0.5)

                pyautogui.click(active.hero)
                pyautogui.click(active.hero)


                screen = ImageGrab.grab()
                obj = screen.load()
                flag1 = 0
                for i in range(913, 973):#для Д
                    if flag1 == 1:
                        break
                    for j in range(914, 932):
                        if obj[i,j] == (43,80,60):
                            print("Игра закончилась, выходим", time.clock()-start_time)
                            flag1 = 1
                            pyautogui.click(948, 907)
                            break


                if out == 1:
                    break
                time.sleep(20)
        elif side == "dire":
            while True:
                if flag1 == 1:
                    break
                screen = ImageGrab.grab()
                obj = screen.load()
                if obj[1583, 1021] == (80, 88, 88) and obj[1584, 1021] == (80, 88, 88) and obj[1585, 1021] == (81, 89, 89):
                    print("Во время игры кто - то вылетел, заново", time.clock() - start_time)
                    break
                elif obj[1891, 1049] == (135, 159, 204):
                    print("Никто не вызывает куру, мы ее вызываем", time.clock() - start_time)
                    press(active.deliver)
                elif obj[1692, 885] == (142, 163, 201):
                    print("Забираем предметы из тайника")
                    pyautogui.click(1692, 885)
                else:
                    PressKey(active.shift)
                    press(active.deliver)
                    ReleaseKey(active.shift)
                #проверка тараски
                if taras == 0:
                    pyautogui.click(items.shop)
                    pyautogui.click(items.best)

                    screen = ImageGrab.grab()
                    obj = screen.load()
                if obj[1765, 630] == (205, 150, 7) and taras == 0:
                    print("Попали сюда?")
                    while True:
                        pyautogui.click(active.secret_d, button='right')
                        screen = ImageGrab.grab()
                        obj = screen.load()
                        if obj[1677, 1044] == (165, 112, 0):
                            print("Попали и сюда")
                            press(active.esc)
                            time.sleep(1)
                            pyautogui.click(items.shop)
                            time.sleep(1)
                            pyautogui.click(1757, 587)
                            time.sleep(1)
                            pyautogui.click(1679, 799, button='right')
                            time.sleep(1)
                            press(active.esc)
                            taras = 1
                            break
                        elif obj[1583, 1021] == (80, 88, 88) and obj[1584, 1021] == (80, 88, 88) and obj[1585, 1021] == (81, 89, 89):
                            out = 1
                            break
                else:
                    press(active.esc)
                if out == 1:
                    break
                if which_lvl() == "лвл 1":
                    print("лвл 1")
                    pyautogui.click(active.skill3)
                if which_lvl() == "лвл 2":
                    print("лвл 2")
                    pyautogui.click(active.skill1)
                if which_lvl() == "лвл 3":
                    print("лвл 3")
                    pyautogui.click(active.skill3)
                if which_lvl() == "лвл 4":
                    print("лвл 4")
                    pyautogui.click(active.skill1)
                if which_lvl() == "лвл 5":
                    print("лвл 5")
                    pyautogui.click(active.skill3)
                if which_lvl() == "лвл 6":
                    print("лвл 6")
                    pyautogui.click(active.skill1)
                if which_lvl() == "лвл 7":
                    print("лвл 7")
                    pyautogui.click(active.skill3)
                if which_lvl() == "лвл 8":
                    print("лвл 8")
                    pyautogui.click(active.skill1)
                if which_lvl() == "лвл 9":
                    print("лвл 9")
                    pyautogui.click(active.skill2)
                if which_lvl() == "лвл 10":
                    print("лвл 10")
                    pyautogui.click(active.talant)
                    pyautogui.click(active.talant1)
                if which_lvl() == "лвл 11":
                    print("лвл 11")
                    pyautogui.click(active.skill2)
                if which_lvl() == "лвл 12":
                    print("лвл 12")
                    pyautogui.click(active.skill2)
                if which_lvl() == "лвл 13":
                    print("лвл 13")
                    pyautogui.click(active.skill2)
                if which_lvl() == "лвл 15":
                    print("лвл 15")
                    pyautogui.click(active.talant)
                    pyautogui.click(active.talant2)
                if which_lvl() == "лвл 20":
                    print("лвл 20")
                    pyautogui.click(active.talant)
                    pyautogui.click(active.talant3)
                if which_lvl() == "лвл 25":
                    print("лвл 25")
                    pyautogui.click(active.talant)
                    pyautogui.click(active.talant4)

                while obj[ 1002 , 921 ] ==  (98, 66, 5):
                    screen = ImageGrab.grab()
                    obj = screen.load()
                    pyautogui.click(active.skill3)
                    time.sleep(0.3)
                    print("Прокачали 3 талант")
                while obj[ 872 , 920 ] ==  (100, 68, 5):
                    screen = ImageGrab.grab()
                    obj = screen.load()
                    pyautogui.click(active.skill1)
                    time.sleep(0.3)
                    print("Прокачали 1 талант")
                while obj[ 939 , 920 ] ==  (100, 67, 5):
                    screen = ImageGrab.grab()
                    obj = screen.load()
                    pyautogui.click(active.skill2)
                    time.sleep(0.3)
                    print("Прокачали 2 талант")
                while obj[ 1065 , 918 ] ==  (99, 66, 5):
                    screen = ImageGrab.grab()
                    obj = screen.load()
                    pyautogui.click(active.skill4)
                    time.sleep(0.3)
                    print("Прокачали 4 талант")

                screen = ImageGrab.grab()
                obj = screen.load()
                PressKey(active.shift)
                pyautogui.moveTo(Coor_d.one)
                press(active.attack)
                pyautogui.moveTo(Coor_d.two)
                press(active.attack)
                pyautogui.moveTo(Coor_d.three)
                press(active.attack)
                if can != 1:
                    if obj[601, 1053] == (64, 27, 1) and obj[602, 1053] == (87, 40, 2) and  obj[603, 1053] == (110, 52, 3) and obj[604, 1053] == (128, 61, 4) and obj[605, 1053] == (191, 173, 119) and obj[606, 1053] == (180, 157, 105) and obj[607, 1053] == (128, 62, 4) and obj[608, 1053] == (118, 57, 3) and obj[609, 1053] == (118, 58, 3) and obj[610, 1053] == (132, 75, 28) and obj[611, 1053] == (190, 172, 118) and obj[612, 1053] == (177, 152, 101) and obj[613, 1053] == (129, 63, 4) and obj[614, 1053] == (120, 58, 4) and obj[615, 1053] == (119, 57, 4) and obj[616, 1053] == (127, 61, 4) and obj[617, 1053] == (164, 133, 86) and obj[618, 1053] == (189, 171, 117) and obj[619, 1053] == (146, 106, 63) and obj[620, 1053] == (104, 49, 3):
                        if obj[ 1142 , 957 ] ==  (148, 147, 117) or obj[ 1207 , 959 ] ==  (164, 162, 133) or obj[ 1268 , 956 ] ==  (158, 157, 127) or obj[ 1140 , 1004 ] ==  (186, 186, 160) or obj[ 1206 , 1004 ] ==  (183, 184, 156) or obj[ 1271 , 1003 ] ==  (163, 163, 134):
                            print("10 лвл и vlad, можем идти на эншетов", time.clock() - start_time)
                            can = 1
                            ensh = 1
                if ensh == 1:
                    pyautogui.moveTo(Coor_d.four)
                    press(active.attack)
                if can == 1:
                    ReleaseKey(active.shift)
                    pyautogui.moveTo(Coor_d.four)
                    press(active.attack)
                    PressKey(active.shift)
                    can = 0
                pyautogui.moveTo(Coor_d.five)
                press(active.attack)
                pyautogui.moveTo(Coor_d.six)
                press(active.attack)
                ReleaseKey(active.shift)

                press(active.bye)
                time.sleep(0.5)
                press(active.bye)
                time.sleep(0.5)
                press(active.bye)
                time.sleep(0.5)
                press(active.bye)
                time.sleep(0.5)

                screen = ImageGrab.grab()
                obj = screen.load()

                if obj[1691, 885] == (142, 163, 201):
                    print("Мы на базе, забираем вещи из тайника", time.clock() - start_time)
                    pyautogui.click(1691, 885)

                pyautogui.click(active.hero)
                pyautogui.click(active.hero)

                screen = ImageGrab.grab()
                obj = screen.load()
                flag1 = 0
                for i in range(913, 973):#для Д
                    if flag1 == 1:
                        break
                    for j in range(914, 932):
                        if obj[i,j] == (43,80,60) or obj[i,j] == (64,10,2):
                            print("Игра за dire закончилась, выходим", time.clock()-start_time)
                            flag1 = 1
                            pyautogui.click(948, 907)
                            break
                if out == 1:
                    break
                time.sleep(20)
    continue















