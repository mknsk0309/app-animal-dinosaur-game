# VSCode DevContainer の使い方

このプロジェクトはVSCode DevContainerを使用して、一貫した開発環境を提供しています。これにより、どのマシンでも同じ環境でコードを実行・開発することができます。

## 前提条件

以下のソフトウェアがインストールされている必要があります：

1. [Visual Studio Code](https://code.visualstudio.com/)
2. [Docker Desktop](https://www.docker.com/products/docker-desktop)
3. VSCodeの[Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)拡張機能

## 開発環境の起動方法

1. このリポジトリをクローンします：
   ```bash
   git clone https://github.com/mknsk0309/app-animal-dinosaur-game.git
   cd app-animal-dinosaur-game
   ```

2. VSCodeでプロジェクトを開きます：
   ```bash
   code .
   ```

3. VSCodeが開いたら、左下の緑色のアイコンをクリックします。

4. 表示されるメニューから「Reopen in Container」を選択します。

5. VSCodeがDevContainerを構築して起動するのを待ちます（初回は数分かかることがあります）。

6. 環境が準備できたら、ターミナルを開いて開発を始めることができます。

## 開発環境の特徴

このDevContainerには以下の機能が含まれています：

- Python 3.10
- Pygame と必要なすべての依存関係
- Git（バージョン管理）
- コード品質ツール（autopep8, pylint）
- テストツール（pytest）
- 便利なVSCode拡張機能（Python, Pylance, autodocstring など）

## ゲームの実行方法

DevContainer内でゲームを実行するには、ターミナルで以下のコマンドを実行します：

```bash
python main.py
```

## 注意事項

- DevContainer内でPygameを実行する場合、グラフィカルな出力はX11転送を設定しない限り表示されません。
- Windowsの場合は、WSL2とX410などのX11サーバーを使用することで、グラフィカルな出力を表示できます。
- macOSの場合は、XQuartzを使用できます。
- 詳細な設定方法は、各OSのドキュメントを参照してください。

## トラブルシューティング

### グラフィカルな出力が表示されない

DevContainer内でPygameのグラフィカル出力を表示するには、X11転送の設定が必要です：

#### Windows (WSL2) の場合：
1. [X410](https://x410.dev/)などのX11サーバーをインストールして実行
2. WSL2のターミナルで `export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0` を実行
3. `.devcontainer/devcontainer.env` ファイルの `SDL_VIDEODRIVER=dummy` をコメントアウト

#### macOS の場合：
1. [XQuartz](https://www.xquartz.org/)をインストールして実行
2. `.devcontainer/devcontainer.env` ファイルの `SDL_VIDEODRIVER=dummy` をコメントアウト
3. DevContainerの再構築が必要な場合があります

### その他の問題

問題が発生した場合は、以下を試してください：

1. VSCodeを再起動
2. DevContainerを再構築（コマンドパレットから「Rebuild Container」を選択）
3. Dockerを再起動
