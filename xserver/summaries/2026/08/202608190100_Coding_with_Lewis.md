# 📺 AWSが無関係の利用者に25億ドルを請求してしまった話

## 📋 動画情報

- **タイトル**: The Time When AWS Billed Random People for $2.5 Billion
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=AhA_m6OShi8](https://www.youtube.com/watch?v=AhA_m6OShi8)
- **動画ID**: AhA_m6OShi8
- **公開日**: 2026年08月19日 01:00
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

AWSのダッシュボードに、普段は月5ドル未満しか払っていないような利用者に対して25億ドルという請求額が表示され、当然のようにパニックが起きた出来事を取り上げた動画です。  
クラウドホスティングを使ったことがある人なら、ダッシュボードを開いて請求額の末尾にゼロが数個増えているのを見たときのあの嫌な感じ（EC2インスタンスの止め忘れ）は分かるはずだ、と語られます。  
ネット上では他のユーザーからも同じ表示を見たという声が上がり、「そんな金額になるほど一体何をしていたのか」と話題になりました。  
その後Amazonが原因を公表し、正体は請求見積もりサブシステム内の単価のバグでした。実際に課金されたわけではなくダッシュボードの数字が誤っていただけで、すぐに修正され、誰も25億ドルを支払ってはいません。  

## ⭐ 重要なポイント

- AWSが、普段は月5ドル未満程度の支払いしかしていない一般の利用者に対して、25億ドルの請求を表示した。  
- 同じ現象を見たという報告がネット上の他のユーザーからも相次ぎ、「これほどの額になる使い方とは何なのか」と騒ぎになった。  
- Amazonが公表した根本原因は、estimated billing（請求見積もり）サブシステム内の単価計算のバグだった。  
- 重要なのは「見積もり」の側で起きた不具合だという点で、実際に課金されたわけではなく、ダッシュボードに出る数字が誤っていただけ。  
- 不具合は速やかに修正され、この巨額の請求を実際に支払った人はいない。  

## 📖 詳細内容

### 🎬 導入

AWS just told random people that they owe $2.5 billion to people who normally pay like under $5 a month for AWS. And this led to obvious panic. If you've ever used a cloud hosting service before, then you know that dread feeling of opening up your dashboard and seeing a couple of extra zeros at the end of your bill. You forgot to turn off your EC2 instance. So, other people around the internet said that they started seeing it, too.

### 📋 背景・概要

What were people even doing for things that cost that much? And then Amazon posted and cleared things up with the real root cause of the issue, a unit pricing bug inside the estimated billing subsystem. Now, important estimated billing, so people weren't actually getting charged, but the numbers on the dashboard were wrong essentially. Still scary though. Of course, this was fixed quickly and nobody paid that billion dollars.

### ⭐ 主要ポイント

Well, hopefully at least. I mean, come on. Does Bezos need another yacht?

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年08月19日

</div>
