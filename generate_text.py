def generate_text(temperature, humidity):
    # 音声メッセージを生成するためのテキスト
    wbgt = int(0.735*temperature + 0.0374*humidity + 0.00292*temperature*humidity-4.064)
    if wbgt >= 31:
        guideline = f"外出はなるべく避け、涼しい室内に移動しましょう。\n高齢者においては安静状態でも熱中症を発生する危険性が大きいです。注意してください。\nまた、屋外での運動は原則中止しましょう。"
    else:
        if wbgt >= 28:
            guideline = f"熱中症の危険性が高いので、激しい運動は控えましょう。\n高齢者においては安静状態でも熱中症を発生する危険性が大きいです。注意してください。\nまた、屋外での運動では10～20分おきに休憩をとり、水分・塩分の補給を行ましょう。\n暑さに弱い人※は運動を軽減または中止しましょう。"
        else:
            if wbgt >= 25:
                guideline = f"運動や激しい作業をする際は定期的に充分な休息を取り入れましょう。\n熱中症の予防のため、適宜、水分・塩分を補給し、激しい運動では、30分おきくらいに休憩をとりましょう。"
            else:
                guideline = f"熱中症の危険は小さいですが、激しい運動や重労働時には発生することがあります。\n適宜、休憩をとりましょう。"


    message = f"現在の温度は {temperature} 度、湿度は {humidity} パーセントです。\n\n気温から計算される暑さ指数は{wbgt} です。\n\n" + guideline

    return message
