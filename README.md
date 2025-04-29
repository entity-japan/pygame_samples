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
>https://github.com/user-attachments/assets/bc66b103-f3f1-4975-91f8-518f76db3ff6

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
>https://github.com/user-attachments/assets/cb0aeea7-2caa-4144-9718-f821a8e35400

## demo_LCD_font.py
### 1、フォントの追加

*0から3の数字のフォントしかないので、4から9のフォントを追加します*

*lcd_font_pg.pyに書き込む↓*
>~~~
>LCD_3 = (0, 1, 1, 1, 0,
>        1, 0, 0, 0, 1,
>        0, 0, 0, 0, 1,
>        0, 1, 1, 1, 0,
>        0, 0, 0, 0, 1,
>        1, 0, 0, 0, 1,
>        0, 1, 1, 1, 0)
>
>LCD_4 = (0, 0, 0, 1, 0,
>        0, 0, 1, 0, 0,
>        0, 1, 0, 1, 0,
>        1, 0, 0, 1, 0,
>        1, 1, 1, 1, 1,
>        0, 0, 0, 1, 0,
>        0, 0, 0, 1, 0)
>
>LCD_5 = (1, 1, 1, 1, 1,
>        1, 0, 0, 0, 0,
>        1, 0, 0, 0, 0,
>        1, 1, 1, 1, 0,
>        0, 0, 0, 0, 1,
>        0, 0, 0, 0, 1,
>        1, 1, 1, 1, 0)
>
>LCD_6 = (0, 0, 1, 0, 0,
>        0, 1, 0, 0, 0,
>        1, 0, 0, 0, 0,
>        1, 1, 1, 1, 0,
>        1, 0, 0, 0, 1,
>        1, 0, 0, 0, 1,
>        0, 1, 1, 1, 0)
>
>LCD_7 = (1, 1, 1, 1, 1,
>        1, 0, 0, 0, 1,
>        1, 0, 0, 0, 1,
>        0, 0, 0, 1, 0,
>        0, 0, 1, 0, 0,
>        0, 0, 1, 0, 0,
>        0, 1, 0, 0, 0)
>
>LCD_8 = (0, 1, 1, 1, 0,
>        1, 0, 0, 0, 1,
>        1, 0, 0, 0, 1,
>        0, 1, 1, 1, 0,
>        1, 0, 0, 0, 1,
>        1, 0, 0, 0, 1,
>        0, 1, 1, 1, 0)
>
>LCD_9 = (0, 1, 1, 1, 0,
>        1, 0, 0, 0, 1,
>        1, 0, 0, 0, 1,
>        0, 1, 1, 1, 1,
>        0, 0, 0, 0, 1,
>        0, 0, 0, 1, 0,
>        0, 0, 1, 0, 0)
>
>LCD_font_styles = (LCD_0, LCD_1, LCD_2, LCD_3, LCD_4, LCD_5, LCD_6, LCD_7, LCD_8, LCD_9)
>~~~

*そして、表示する数字を決めます*

*demo_LCD_font_01.pyに書き込む↓*
>~~~
>code = int((x / 8) % 10)
>~~~

*変更後↓*
>https://github.com/user-attachments/assets/e03b6e40-56f6-4997-a91b-c8e9e837a431

### 2、桁の追加

*桁を追加します*

*今回は、十の位を作ります*

>~~~
>def LCD_display(x, y):
>    code = int((x / 8) % 10)
>    code1 = int((x / 10 / 8) % 10)
>    text1, rect1 = font1.render(str((10*code1)+code), WHITE)
>    rect1.center = (x, y)
>    screen.blit(text1, rect1)
>    # LCD sim
>    lcd1.update_col(col=0, code=code1)
>    lcd1.update_col(col=1, code=code)
>~~~

*変更後↓*
>https://github.com/user-attachments/assets/35445338-9389-4ffd-8e33-684063f0bb5c

## LCDフォントで時刻、日付を表示する

*変更前↓
>https://github.com/user-attachments/assets/e75a65ac-e356-4e49-917c-c742e4a8f280

### 1、フォントの追加

*新たに「：」と「ー」のフォントを追加します*

*lcd_font_pg.pyに書き込む↓*
>~~~
>LCD_10 = (0, 0, 0, 0, 0,
>          0, 1, 1, 0, 0,
>          0, 1, 1, 0, 0,
>          0, 0, 0, 0, 0,
>          0, 1, 1, 0, 0,
>          0, 1, 1, 0, 0,
>          0, 0, 0, 0, 0,)
>
>LCD_11 = (0, 0, 0, 0, 0,
>          0, 0, 0, 0, 0,
>          0, 0, 0, 0, 0,
>          1, 1, 1, 1, 1,
>          0, 0, 0, 0, 0,
>          0, 0, 0, 0, 0,
>          0, 0, 0, 0, 0,)
>
>LCD_font_styles = (LCD_0, LCD_1, LCD_2, LCD_3, LCD_4, LCD_5, LCD_6, LCD_7, LCD_8, LCD_9, LCD_10, LCD_11)
>~~~

### 2、LCDフォント表示の要素を抜き出し、demo_03.pyに取り込む

*demo_lcd_font.pyからLCDフォント表示の要素を抜き出し、demo_02.pyを複製して作ったdemo_03.pyに取り込みます*

>~~~
>font1 = pygame.freetype.Font("fonts/natumemozi.ttf", 48)>
>
>lcd1 = LCD_font(screen)
>lcd1.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=(120, 200, 250), COLOR_OFF=GRAY)
>lcd1.init_row(X_ORG=2, Y_ORG=2, COL_INTV=6)
>
>
>def LCD_display(x, y):
>     lcd1.update_col(col=0)>
>
>lcd2 = LCD_font(screen)
>lcd2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=RED, COLOR_OFF=GRAY)
>lcd2.init_row(X_ORG=2, Y_ORG=17, COL_INTV=6)
>
>def LCD_display(x, y):
>    lcd2.update_col(col=0)
>~~~

### 3、LCDフォントで時刻、日付を表示する

*LCDフォントで時刻と日付を表示します*

*lcd1が時刻、lcd2が日付です↓*
>~~~
>lcd1.update_col(col=0, code=dt_now.hour // 10)
>lcd1.update_col(col=1, code=dt_now.hour % 10)
>lcd1.update_col(col=2, code=10)
>lcd1.update_col(col=3, code=dt_now.minute // 10)
>lcd1.update_col(col=4, code=dt_now.minute % 10)
>lcd1.update_col(col=5, code=10)
>lcd1.update_col(col=6, code=dt_now.second // 10)
>lcd1.update_col(col=7, code=dt_now.second % 10)
>
>lcd2.update_col(col=0, code=int(str(dt_now.year)[0]))
>lcd2.update_col(col=1, code=int(str(dt_now.year)[1]))
>lcd2.update_col(col=2, code=int(str(dt_now.year)[2]))
>lcd2.update_col(col=3, code=int(str(dt_now.year)[3]))
>lcd2.update_col(col=4, code=11)
>lcd2.update_col(col=5, code=dt_now.month // 10)
>lcd2.update_col(col=6, code=dt_now.month % 10)
>lcd2.update_col(col=7, code=11)
>lcd2.update_col(col=8, code=dt_now.day // 10)
>lcd2.update_col(col=9, code=dt_now.day % 10)
>~~~

*変更後↓*
>https://github.com/user-attachments/assets/26948674-a1eb-490a-ada3-7ec6d9601c1f