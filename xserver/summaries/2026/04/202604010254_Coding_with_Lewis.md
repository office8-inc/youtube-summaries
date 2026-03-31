# 📺 JavaScriptの歴史上最も衝撃的なサプライチェーン攻撃

## 📋 動画情報

- **タイトル**: The most INSANE attack in JavaScript history?
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=I_EehEQ3sYI](https://www.youtube.com/watch?v=I_EehEQ3sYI)
- **動画ID**: I_EehEQ3sYI
- **公開日**: 2026年04月01日 02:54
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

週に3億回以上インストールされているJavaScriptの人気ライブラリ「Axios」が、高度に計画されたサプライチェーン攻撃によって侵害されました。攻撃者はメンテナーのNPMアカウントを乗っ取り、悪意のある依存関係を含む新バージョンを公開することで、CIチェックをすべて回避しました。直接コードに悪意あるコードを埋め込むのではなく、インストール後に実行されるスクリプト（postinstall）を通じてリモートアクセス型トロイの木馬（RAT）をインストールするという巧妙な手法が使われました。Axiosは毎秒500回以上インストールされており、たった2時間の間に数万台のマシンが侵害された可能性があります。セキュリティ意識の高い開発者・エンジニア向けに、オープンソースサプライチェーンの脆弱性を警告する内容です。

## ⭐ 重要なポイント

- **Axiosが高度なサプライチェーン攻撃で侵害**：メンテナーのNPMアカウントが乗っ取られ、悪意ある依存関係を含む新バージョンが公開された
- **直接コード改ざんではなく依存関係経由**：パッケージ本体には悪意あるコードを入れず、追加された依存関係のpostinstallスクリプトでRATをインストールする巧妙な手法
- **CI/CDを完全に回避**：公式メンテナーアカウントからの公開であったため、継続的インテグレーションのセキュリティチェックを突破してしまった
- **被害規模が甚大な可能性**：Axiosは毎秒500回超インストールされており、わずか2時間でも膨大な台数が感染リスクにさらされた
- **オープンソースのサプライチェーンセキュリティの課題**：今回の攻撃は偶発的なものではなく、明らかに計画的・意図的な高度な攻撃であり、開発者は依存関係の管理に一層の注意が必要

## 📖 詳細内容

### 🎬 導入

One of the most insane things just happened in the world of programming. Axios, the JavaScript package that's installed over 300 million times per week, was compromised completely by a sophisticated attack. Someone hijacked a lead maintainers MPM account, swapped email addresses, and then published two new versions of the Axios library. And because they're on the lead maintainers account, it was able to bypass any continuous integration or delivery, just going straight to production. like any good programmer would.

### 📋 背景・概要

But here's where it actually gets insane. There was no malicious code that was directly injected in the package itself. It was just a dependency added. So when Axios is installed anywhere, aka 300 million times per week, it installs that dependency. But then that dependency runs a postinstall script which installs a remote access Trojan onto your operating system, giving the anyone full access.

### ⭐ 主要ポイント

hits beyond bonkers. And this was honestly caught pretty quickly, but quick maths here. Axios is being installed over 500 times per second. So even if it was like 2 hours, say, that's a lot of machines that could potentially be compromised. This level of attack doesn't just happen by accident.

### 📝 詳細説明

It was clearly premeditated. Ball for more.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年04月01日

</div>
