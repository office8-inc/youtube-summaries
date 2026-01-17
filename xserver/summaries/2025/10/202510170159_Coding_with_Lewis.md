# 📺 9つのAIモデルで同じゲームを作らせた結果（予想外の展開）

## 📋 動画情報

- **タイトル**: 9 AI Models Built the Same Game (Results Were Unexpected)
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=07YLWTDdStg](https://www.youtube.com/watch?v=07YLWTDdStg)
- **動画ID**: 07YLWTDdStg
- **公開日**: 2025年10月17日 01:59
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

GPT-5、Claude Sonnet 4、Gemini 2.5 Pro、DeepSeek R1など9つのAIモデルに同じ3Dレーシングゲームを作らせ、その性能を徹底比較した実験動画です。各モデルのコード品質、バグ対応能力、コスト効率、クリエイティブな判断力を実際のプロジェクトで検証しています。AIコーディングエージェントの実力を知りたい開発者、ローカルLLMに興味があるエンジニア、AI時代のプログラミングの未来を考えたい方に最適な内容です。

## ⭐ 重要なポイント

- **GPT-5の意外な弱点**: 約3.53ドルのコストがかかり、指示の理解に苦戦。手取り足取りのガイダンスが必要で期待外れの結果に
- **Claude Opus 4.1の高コスト**: プラン作成だけで21セント課金。非常にパワフルだが、コスト効率は最悪。ただしリアルタイムで変更を反映できるのは面白い体験
- **Gemini 2.5 Proのコスパ**: 低価格でマイクロマシン風のユニークなデザインを生成。ただしコード品質に問題があり、変更後に動作不能に
- **DeepSeek R1の超低価格**: ほぼ無料だが、バグが多く手動での修正が必要。コストを抑えたい場合の選択肢
- **ローカルモデルの可能性**: Qwen 3 Coder（30B）やGPT-OSS（120B）はVRAM要件が高いが、Windows AI Foundryを使えば高速動作。プライバシーとスピードを重視するなら有力な選択肢

## 📖 詳細内容

### 🎬 導入

90% of programmers are using AI in their job. CEOs are replacing programmers with coding agents like Claude Code. But is that a mistake? In today's video, I'll be ranking a bunch of different AI's ability to create 3D racing game to see if we're truly cooked. Now we all know about AI coding agents.

### 📋 背景・概要

At first it was the auto complete, then the chat, but now it's the agent. It's all about the agents letting AI talk to itself for hours until it decided it broke your code base enough. I'll be using open code to test these out. So let's just get started. Create a fully playable 3D racing game in H-T-M-L-C-S-S and JavaScript requirements.

### ⭐ 主要ポイント

Use three js for 3D graphics. Implement a racing car that the player controls. Like all true gamers do. Create a looping race track with visible boundaries. Walls add acceleration, deceleration and turning speed indicator on screen.

### 📝 詳細説明

Add at least three AI opponent cars that race around the track collision detection between all cars and tracks. A lap counter that tracks three laps to win. 3, 2, 1, go. The big boy on the block, GPT five. Fun fact, you actually have to verify your identity with this in order to use it.

### 💡 実例・デモ

You know, the racing game could lead to serious federal felonies. Now, GPT five actually took a very long time and at times it just didn't really understand how to fix the issue like at all. A big issue was that it was just not able to understand my instructions and then differentiate between what my instructions should do. So I just don't even know about this one. Overall though, it costs about $3 and 53 cents.

### 🔧 技術的詳細

And so for a large language model that's actually, that's pretty good price all, all said and do, but I did feel like I had to hold his hand for a lot of the results that I didn't even want in the end. Anyway. Maybe they'll fix this in the upcoming update, but let's, let's see. Sonnet four is one of the most popular large language models for these type of tasks. In fact, it's Claude Code, it's what's being used for the most part.

### 🎯 応用例

However, it took a very long time to get the result that I wanted. It cost me $2 and 77 cents and it was just a buggy mess throughout and it took multiple attempts to do it as well. Opus 4.1 is a very, very beefy model and very, very expensive. Something I noticed right off the bat is that I got charged 21 cents just to make a plan on how they should work. Now this came obviously, uh, it sucks.

### 💭 考察

It's not really good, um, but it was actually kind of fun playing the game and doing it while the agent was making changes in the background. I would always have like a new version ready to play. It was like kind of like a warrior aware or something. It was honestly interesting. Gemini 2.5 Pro was really cheap in terms of pricing.

### 📌 まとめ

However, it did take a lot of creative liberties, which I'm honestly not too mad about. It kind of did like a micro machine style game, which I thought was pretty cool. The code quality was questionable. It separated the user car and AI car into separate files despite using classes. And like, I'm not a game dev here, right?

### ✅ 結論

But this doesn't seem like really efficient whatsoever. And for the most part I liked things being in separate files, but maybe in folders too. You know, like not everything has to be in one giant folder. The one thing though is that I tried to change the look of it and then everything just broke with this loading screen and it just really couldn't even recover from there. But that being said, I am somewhat impressed by Gemini 2.5 Pro, but at the same time felt like it completely shot itself in the foot and was unable to walk after that.

### 📚 追加情報

So yeah, to run some of these models locally, I'm going to use Windows AI Foundry who is the sponsor of today's video. Windows AI Foundry is a platform to help you build applications from selecting models, fine tuning and deploying across different hardware and cloud providers. There are Windows AI APIs that you can use to integrate large language models into your application natively while having an easy solution to switch to a cloud model if needed. PHI Silica is a 3.3 billion parameter model that is capable of tasks requiring text Intelligence. Foundry Local lets you integrate open source models from places like Azure, AI Foundry, or hugging face to run locally on your device while taking advantage of your hardware to accelerate.

### 🔖 補足

Whether that's a GPU and MPU or a CPU Windows ML allows you to take custom models and run it directly on your machine. With hardware acceleration, your code will then run on natively on the A-C-P-U-G-P-U and MPU. So whether you want to just test out AI locally, like me on your machine or start getting deep in the integration process of these AI models with your applications, windows AI Foundry is the platform to get your AI app started quickly. Thanks again to Microsoft for sponsoring today's video. Deep Seek R one just took forever, but wow, the price was basically nothing, but I mean like you're spending money to get nothing either.

### 🎨 セクション 13

One issue though is that it just constantly kept running into bugs that I just wasn't able to fix. I had to go into the code myself at times and play around with it to get it to just work, to even just get off of a loading screen. Can you believe that coding with Lewis actually had to do some coding on his channel for once? Quin three coder is one of the most popular open source models in agents right now. This model is too beefy for a regular consumer device, but you can get lightning speeds on specific networks.

### 🚀 セクション 14

Now this model got really ambitious with everything. It included a quick race, a championship, a garage feature, like this is GTA six. Don't make any mistakes. The issue is that it didn't really get the core gameplay right, which, you know, always focus on mechanics first. That's what the game devs told me, and that's something I'm noticing a lot right now with these models.

### ⚡ セクション 15

I think part of it is just hard for the feedback loop that it's getting. It can't really play the game even when you're adding like these playwright MCP servers and stuff. It just isn't doing it the same way. But overall though, I could see this being a huge help if you already built a game, which is why I love the coding agents to begin 88 00:06:54,50 --> 00:06:54,310 with. Now, let's use G-P-T-O-S-S 20 B from Foundry Local.

### 🌟 セクション 16

Let's just run that on the command line and get going. G-P-T-O-S-S 20 B runs lightning fast. When you do it locally. You also just don't have to worry about the latency either. This model does require like 16 gigabytes of V ramm though, so take that in mind.

### 🎬 セクション 17

Now, this didn't really exactly get anything that I wanted correctly, but it somehow kind of made a fun game on its own, which I mean, I'm not too mad about. This model would definitely be better suited for something like an auto complete in your code editor or Word document. G-P-T-O-S-S one 20 B did a little bit better than the 20 billion parameters one. I mean, it's got a hundred more billion parameters, right? But still had issues trying to get the controls to work.

### 📋 セクション 18

But similarly, it had a new game that was a lot of fun, like throwing the red brick around. But this time the camera follows it. Something I do like is that the physics feel great in these models, which might also just come from the native implementation of three Js, but I mean, who, who knows? Quinn three coder 30 B runs extremely fast on a computer. However, this also takes a lot of VAM.

### ⭐ セクション 19

Something I really like about this model is that it is trained to work on these age agentic type of workflows, and this one actually did pretty well. I really enjoy the look that it had. It was a little bit more complex than the other one, but the, I guess the final result was still a bit strange, you know, and it did struggle. This one had a lot of handholding to do, which not a fan. Something I learned is that when it comes to actually creating things full on, the only thing that AI is great at is giving you a starting point.

### 📝 セクション 20

A lot of people are worried about AI taking our jobs, but really I think AI has just proven to be a great tool that will improve your productivity as a developer. And this is why I think local large language models are going to be so useful considering the speed, intelligence, and privacy. If you wanna run local AI models, make sure you check out Windows, AI Foundry and use Foundry local to run them in your command line. What models would you want to see next? Let me know.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年01月17日

</div>
