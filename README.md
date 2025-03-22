# pygame_samples
## demo_01.py の改造

*↓変更前*
![Image](https://github.com/user-attachments/assets/f4d60e5f-d257-4e7a-9b49-4a29a0051bd5)

### 1、ウィンドウサイズの変更

*ウィンドウサイズを変更します*

*変更前*
>~~~
>screen = pygame.display.set_mode([640, 480])
>~~~

*変更後*
>~~~
>screen = pygame.display.set_mode([800, 640])
>~~~

### 2、タイトルバーの変更

*タイトルバーを変更します*

*今回は、最後に「やで～」をつけました*

*変更前*
>~~~
>pygame.display.set_caption("pygame demo - window title here")
>~~~

*変更後*
>~~~
>pygame.display.set_caption("pygame demo - window title here やで～")
>~~~

### 3、背景色の変更

*背景色を変更します*

*今回は、黄土色のような色にしました*

*変更前*
>~~~
>screen.fill((238, 238, 170))
>~~~

*変更後*
>~~~
>screen.fill((220, 190, 75))
>~~~

*↓1~3の変更後*
![Image](https://github.com/user-attachments/assets/966b1bb2-bd4a-4e8b-8132-637857835587)

### 4、大きな円（薄紫色の円）の場所＆色の変更

*大きな円の場所と色を変更します*

*変更前*
>~~~
>pygame.draw.circle(screen, (176, 176, 222), (320, 240), 120)
>~~~

*変更後*
>~~~
>pygame.draw.circle(screen, (0, 255, 255), (500, 400), 200)
>~~~

*プログラムの<ins>screen</ins>の後に続く数字ですが、*
*最初のかっこはカラーコードが入ります。例→(0, 255, 255)*
*そのあとに続くかっこにはx座標、y座標、大きさがそれぞれ入ります*
*((x,y),大きさ)となります*

### 5、小さな円（ピンク色の円）の場所＆色の変更

*小さな円の場所と色を変更します*

*変更前*
>~~~
>pygame.draw.circle(screen, (222, 176, 222), (120, 120), 20)
>~~~

*変更後*
>~~~
>pygame.draw.circle(screen, (192, 192, 192), (500, 400), 125)
>~~~

### 6、小さな円（ピンク色の円）の場所＆色の変更

*5で変更した円と色も場所も同じなので重なってしまっていますね（笑）*

*この円の場所と色を変更します*

*変更前*
>~~~
>pygame.draw.circle(screen, (222, 176, 222), (120, 120), 20)
>~~~

*変更後*
>~~~
>pygame.draw.circle(screen, (0, 255, 0), (500, 400), 50)
>~~~

### 7、ドットマトリクスの色＆縦と横の長さの変更

*ドットマトリクスの色と縦と横の長さを変更します*

*今回は、ドットマトリクスの色を動くドットはシアン、それ以外は白にしました*

*縦と横の長さは8×10にしました*

*色*
>~~~
>color_on = (0, 255, 255)
>color_off = (255, 255, 255)
>~~~

*縦の長さ*
>~~~
>for x0 in range(5):
>~~~

*横の長さ*
>~~~
>for y0 in range(7):
>~~~

*↓1~7の変更後*
![Image](https://github.com/user-attachments/assets/03ee0265-4a93-477b-a665-ccfcfdd50b33)

### 8、ドットマトリクスのドット移動を改造

*↓変更前*
https://github.com/user-attachments/assets/bc66b103-f3f1-4975-91f8-518f76db3ff6

*ドットマトリクスのドット移動を改造します*

*具体的にはドットマトリクスのドットを右下から左上まで、すべての位置で動くようにします*

*まず、xを1ずつ増やす*
>~~~
>x1 += 1
>~~~

*次に、ドットが端についたら下の段にいくようにする*

*変更前*
>~~~
>if x1 > 4:
>    x1 = 0
>~~~

*変更後*
>~~~
>if x1 > 4:
>    x1 = 0
>    y1 += 1
>~~~

*右下までたどり着いたら左上にいくようにする*

*↓を追加*
>~~~
>if y1 > 6:
>    y1 = 0
>~~~

*↓変更後*
https://github.com/user-attachments/assets/cb0aeea7-2caa-4144-9718-f821a8e35400