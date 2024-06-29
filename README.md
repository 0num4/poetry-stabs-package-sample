# poetry-stabs-package-sample

パッケージ公開サンプル

```
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish -r poetry-stabs-package-sample
```

# 型を付ける

`addは型がついている、つまりちゃんとannotateしていればpyiとかpy.typedとかは必要ない`
自分の理解は最初こうだったんですが mypy はこけてしまう！！

```
❯ mypy awesome-poetry-cache/
awesome-poetry-cache/awesome_poetry_cache/sample.py:1: error: Skipping analyzing "poetry_stabs_package_sample": module is installed, but missing library stubs or py.typed marker  [import-untyped]
awesome-poetry-cache/awesome_poetry_cache/sample.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 3 source files)
```

https://blog.ymyzk.com/2018/09/creating-packages-using-pep-561/

# テストを書く

# awesome linters

# documents

# publish package

pypa/gh-action-pypi-publish@release/v1 を使うと公開できる、pypi とは odic で連携してるっぽいので事前に pypi の設定が必要
https://docs.github.com/ja/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-pypi

## poetry publish をする

poetry に token の設定が必要

普通に公開しようとすると夏期のようなエラーが出た

```
❯ poetry publish --build -r testpypi
There are 2 files ready for publishing. Build anyway? (yes/no) [no] yes
Building poetry-stabs-package-sample (0.1.0)
  - Building sdist
  - Built poetry_stabs_package_sample-0.1.0.tar.gz
  - Building wheel
  - Built poetry_stabs_package_sample-0.1.0-py3-none-any.whl

Publishing poetry-stabs-package-sample (0.1.0) to testpypi
 - Uploading poetry_stabs_package_sample-0.1.0-py3-none-any.whl FAILED

HTTP Error 403: Invalid or non-existent authentication information. See https://test.pypi.org/help/#invalid-auth for more information. | b'<html>\n <head>\n  <title>403 Invalid or non-existent authentication information. See https://test.pypi.org/help/#invalid-auth for more information.\n \n <body>\n  <h1>403 Invalid or non-existent authentication information. See https://test.pypi.org/help/#invalid-auth for more information.\n  Access was denied to this resource.<br/><br/>\nInvalid or non-existent authentication information. See https://test.pypi.org/help/#invalid-auth for more information.\n\n\n \n'

```

```
poetry config pypi-token.testpypi "pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

通った

```
❯ poetry publish --build -r testpypi
There are 2 files ready for publishing. Build anyway? (yes/no) [no] yes
Building poetry-stabs-package-sample (0.1.0)
  - Building sdist
  - Built poetry_stabs_package_sample-0.1.0.tar.gz
  - Building wheel
  - Built poetry_stabs_package_sample-0.1.0-py3-none-any.whl

Publishing poetry-stabs-package-sample (0.1.0) to testpypi
 - Uploading poetry_stabs_package_sample-0.1.0-py3-none-any.whl 100%
 - Uploading poetry_stabs_package_sample-0.1.0.tar.gz 100%

```

# バージョンを上げる

```
poetry version patch
```

上でバージョンを上げても github 上の ci release ではバージョンは上がらなかったので ~~pypi 上のバージョンは git tags のバージョンに依存してそう。pyproject.toml や自動で再デプロイするとバージョンが上がるわけではなさそう~~

そんなことはなくて普通に pyproject.toml に依存してる。ただし*poetry build*を忘れないこと

## pypi にいれる release env みたいなやつ

入れないほうが無難。

## test.pypi は？

めっちゃ flakey。成功するまでリトライするとかするといいかもしれない。ghaction には現在再試行するオプションはなさそうだったので 3 回同じ文を書く脳筋実装をした

```
    - name: publish testpypi
      id: publish
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        repository-url: https://test.pypi.org/legacy/
      continue-on-error: true
    - name: retry publish testpypi
      if: steps.publish.outcome == 'failure'
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        repository-url: https://test.pypi.org/legacy/
      continue-on-error: true
    - name: retry publish testpypi (2nd attempt)
      if: steps.publish.outcome == 'failure'
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        repository-url: https://test.pypi.org/legacy/
      continue-on-error: true
```

# badge

https://zenn.dev/atu4403/articles/howto-poetry-dev#badge%E3%81%AE%E5%8F%96%E5%BE%97
fury.io で取得できる。今は test.pypi なのでできないけど

## その他 tips

content: write を付けないと gh actions 上で該当のリポジトリへ push ができない

```
permissions:
  contents: write
```

## **init**.py で flake8 が import not used エラーを出すやつ

https://stackoverflow.com/questions/31079047/python-pep8-class-in-init-imported-but-not-used
**all**を使える

## ref

https://cylomw.hatenablog.com/entry/2021/01/19/174847
https://blog.ymyzk.com/2018/09/creating-packages-using-pep-561/

## pre-commit について

https://tma15.github.io/blog/2023/01/28/pythonpre-commit%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%82%B3%E3%83%9F%E3%83%83%E3%83%88%E5%89%8D%E3%81%AB%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%82%92%E8%87%AA%E5%8B%95%E6%A4%9C%E6%9F%BB%E3%81%99%E3%82%8B/
https://zenn.dev/nowa0402/articles/79aaeb8db5731c#.vscode%2Fsettings.json

pre-commit は適用した後.py ファイルを編集しないと mypy がデフォルトで発火しない。また、pre-commit-config.yaml が普通に見づらい。

```
user: root …/Owner/work/private/test/poetry-stabs-package-sample on  main [⇡] is 📦 v0.1.8 via 🐍 v3.12.3 (bindsample-py3.12) took 8s
❯ git commit -m "feat: update precommit"
[INFO] Initializing environment for https://github.com/pre-commit/mirrors-mypy.
[INFO] Installing environment for https://github.com/pre-commit/mirrors-mypy.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...............................................................Passed
Check for added large files..............................................Passed
mypy.................................................(no files to check)Skipped
[main d3c82d1] feat: update precommit
 1 file changed, 11 insertions(+), 5 deletions(-)

user: root …/Owner/work/private/test/poetry-stabs-package-sample on  main [!+⇡] is 📦 v0.1.8 via 🐍 v3.12.3 (bindsample-py3.12)
❯ git commit -m "feat: update precommit"
[ERROR] Your pre-commit configuration is unstaged.
`git add .pre-commit-config.yaml` to fix this.

user: root …/Owner/work/private/test/poetry-stabs-package-sample on  main [!+⇡] is 📦 v0.1.8 via 🐍 v3.12.3 (bindsample-py3.12)
❯ git commit -m "feat: update precommit"
Trim Trailing Whitespace.............................(no files to check)Skipped
Fix End of Files.....................................(no files to check)Skipped
Check Yaml...........................................(no files to check)Skipped
Check for added large files..........................(no files to check)Skipped
mypy.................................................(no files to check)Skipped
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

user: root …/Owner/work/private/test/poetry-stabs-package-sample on  main [⇡] is 📦 v0.1.8 via 🐍 v3.12.3 (bindsample-py3.12)
❯ git commit -m "feat: update precommit"
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...........................................(no files to check)Skipped
Check for added large files..............................................Passed
mypy.....................................................................Failed
- hook id: mypy
- exit code: 2

pyproject.toml:1: error: Error importing plugin "pydantic.mypy": No module named 'pydantic'
Found 1 error in 1 file (errors prevented further checking)


```
