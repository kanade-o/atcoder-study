# atcoder-study
AtCoder練習記録2

## Requires

```
pip install -r requirements.txt
```
```
npm install -g atcoder-cli
```

インストール確認
```
acc -h
```
```
oj -h
```

連携確認
トークンセッション貼り付け
```
aclogin
```
```
acc check-oj
```

ログイン
```
acc login
oj login https://beta.atcoder.jp/
```
alias登録
```
alias ojt='oj t -c "python3 main.py"'
alias accs='acc s -- main.py --language 5078'
```

## 使用方法
### 問題ダウンロード
```
acc n abcXXX
```

### テスト
```
ojt
```

### 提出
```
accs
```
