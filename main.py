from cv2 import cv2


def median3na3(img, i, j):
    b = int(int(img[i, j][0]) + int(img[i, j - 1][0]) + int(img[i, j + 1][0]) + int(img[i - 1, j - 1][0]) + int(
        img[i - 1, j][0]) + int(img[i - 1, j + 1][0]) + int(img[i + 1, j + 1][0]) + int(img[i + 1, j - 1][0]) + int(
        img[i + 1, j][0])) / 9
    g = int(int(img[i, j][1]) + int(img[i, j - 1][1]) + int(img[i, j + 1][1]) + int(img[i - 1, j - 1][1]) + int(
        img[i - 1, j][1]) + int(img[i - 1, j + 1][1]) + int(img[i + 1, j + 1][1]) + int(img[i + 1, j - 1][1]) + int(
        img[i + 1, j][1])) / 9
    r = int(int(img[i, j][2]) + int(img[i, j - 1][2]) + int(img[i, j + 1][2]) + int(img[i - 1, j - 1][2]) + int(
        img[i - 1, j][2]) + int(img[i - 1, j + 1][2]) + int(img[i + 1, j + 1][2]) + int(img[i + 1, j - 1][2]) + int(
        img[i + 1, j][2])) / 9
    return b, g, r


def my_filter(img):
    for i in range(5, img.shape[0] - 10):
        for j in range(5, img.shape[1] - 10):
            img[i, j] = median3na3(img, i, j)


def loading_displaying_saving():
    img = cv2.imread('germany.jpg')
    cv2.imwrite('graygermany.jpg', img)
    my_filter(img)
    cv2.imshow('germany', img)
    cv2.imwrite('graygermany.jpg', img)
    cv2.waitKey(0)

loading_displaying_saving()
