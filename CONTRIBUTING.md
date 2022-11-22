# Contributing

해당 레퍼지토리에 기여할 때 누가 어떤 내용에 기여했는지 구분하기 위해 아래의 규칙을 지키면 좋을 거 같습니다.

## Commit Process

1. `main` 브랜치는 최종본만 업로드합니다.
2. `dev` 브랜치에 실질적으로 필요한 모든 코드를 업로드합니다. 기능 개발, 실험은 feat-{기능명}, exp-{실험명}와 같은 브랜치를 만들어서 push하고 dev에 merge합니다.
3. 눈갱 방지를 위해 최소한 코드 에디터가 제공하는 [코드 정리(Linting)](https://code.visualstudio.com/docs/python/linting) 기능을 사용하여 *(VSCode 의 경우 cmd+k+f)* [PEP8](https://peps.python.org/pep-0008/)을 준수하려고 노력해 보기.
4. git commit convention
    - fix : 버그 패치
    - feat : 기능 추가
    - style : Style & Typo, 기능 변경 없이 간단한 변수명, 파일명, 경로변경 등의 작업
    - refactor : 기능 변경 없이 레거시를 리팩터링하는 거대한 작업
    - Docs : 기능 변경 없이 문서 및 주석 수정
    - tests : 테스트 코드 업로드
    - first commit
5. __이슈__, __PR__ 역시 제목은 같은 형식으로 작성합니다.
    
```text
<convention> <한 줄 영문설명> (이슈링크)
# 한 줄 띄우기
<커밋에 대한 본문(선택 사항) 설명(한글)>

```

`example`
```text
fix eda index error fix (#102)

- 박스친 이미지를 출력하는 과정에서 생긴 인덱스 문제를 해결
```


### 참고

- [CONTRIBUTING.md template](https://gist.github.com/PurpleBooth/b24679402957c63ec426)
- [VSCode Linting](https://code.visualstudio.com/docs/python/linting)
- [Python PEP8](https://peps.python.org/pep-0008/)
- [Git commit convention](https://www.conventionalcommits.org/ko/v1.0.0/)
- [Git commit convention reference: FastAPI Template project](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [Sementic versioning](https://semver.org/lang/ko/)
- [Repository convention reference: SSAFY BookFlex project](https://github.com/glenn93516/BookFlex)
