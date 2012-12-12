# gantty - 간트챠트를 위한 컴팩트 신택스

자신이 사용하는 텍스트 에디터로 누구나 쉽게 간트챠트를 작성하자!

gantty는 

## 작성방법

gantty파일은 확장자 .gnty가 붙은 텍스트 파일이다.
다음과 같이 `#` + 문자열 형식으로 주석을 달수 있다.

<pre>
# 이것은 주석문입니다.
</pre>

텍스트의 인코딩을 명시하려면 파일의 첫번째 줄에 다음과 같이 기술한다.

<pre>
# encoding=utf-8
</pre>

gantty에는 하나 이상의 작업이 있어야 한다. 작업은 이름, 시작일, 작업시간, 작업자, 의존 작업 같은 속성들로 이루어 지며, 각 속성 사이는 하나 이상의 공백이 있어야 한다. 하나의 작업은 한 줄로 기술되어야 한다. 작업 전/후의 빈 줄은 무시된다.

작업의 각 속성들을 살펴보자.

### 작업명
작업의 이름을 나타낸다.
다음과 같이 `[` `]`안에 이름을 기술한다.

<pre>
[디자인]
</pre>

### 시작일
시작일은 작업이 시작하는 날짜를 의미한다.
시작일은 작업명 뒤에 다음과 같이 년/월/일 형식으로 기술한다.

<pre>
[디자인] 2012/10/01
</pre>

### 작업시간
작업시간은 작업을 끝내기 위해 필요한 (예상)시간이다. 
작업시간은 시간(h) 일(d) 주(w) 단위로 표기할 수 있다. 
예를 들어 30시간이 필요한 경우 다음과 같이 기술한다.

<pre>
[디자인] 2012/10/01 30h
</pre>

2주가 필요한 경우 다음과 같이 기술한다.

<pre>
[디자인] 2012/10/01 2w
</pre>

*서로 다른 단위를 섞어서 사용하지는 못한다.*

### 작업자
작업을 수행할 사람을 말한다.
작업자는 다음과 같이 `@` + 이름 형식으로 기술 한다.

<pre>
[디자인] 2012/10/01 30h @이수일
</pre>

한명 이상인 경우 이어서 기술한다.

<pre>
[디자인] 2012/10/01 30h @이수일 @심순애
</pre>

### 하위작업
특정 작업이 세부작업으로 나누어지는 경우, 다음과 같이 인던트를 이용해 기술한다.

<pre>
[디자인]
    [레이아웃 디자인] 2012/10/01 10h @이수일
    [버튼 디자인] 2012/10/03 20h @심순애
</pre>

이때 '디자인'을 상위작업, '레이아웃 디자인' '버튼 디자인'을 디자인의 하위작업이라고 한다.

다음의 내용을 주의하자.

* 인던트는 tab이나 space 등을 자유롭게 사용할 수 있으나 한 파일 안에서 일관성을 유지해야 한다.

* 하위작업이 있는 경우 상위작업에는 따로 시작일, 시간, 작업자 같은 정보를 기술하지 않는다.


### 의존작업
어떤 작업을 시작하기 위해 먼저 수행되어야할 작업을 말한다.
의존은 다음과 같이 `->` + 작업명으로 기술한다.

<pre>
[디자인 컨셉 정하기] 2012/09/20 1w @홍길동 -> [디자인]
[디자인]
    [레이아웃 디자인] 2012/10/01 10h @이수일
    [버튼 디자인] 2012/10/03 20h @심순애
</pre>

위의 예는 '버튼을 디자인하기 위해서 먼저 디자인 컨셉을 정해야 한다'는 뜻이 된다.

### 서브젝트

서브젝트는 작업들을 그룹짓기 위해 사용된다. 서브젝트 아래에 하나 이상의 작업이 등록된다.
서브젝트는 다음과 같이 `<` `>` 안에 이름을 기술한다.

<pre>
<웹 개편>
[디자인 컨셉 정하기] 2012/09/20 1w @홍길동 -> [디자인]
[디자인] -> [개발]
    [레이아웃 디자인] 2012/10/01 10h @이수일
    [버튼 디자인] 2012/10/03 20h @심순애
[개발]
    [HTML 코딩] 2012/10/07 20h @성춘향
    [스크립트 개발] 2012/10/10 30h @이몽룡
</pre>

## 샘플파일

다음은 위에서 설명한 내용으로 작성한 완전한 샘플파일이다.

<pre>
# encoding=utf-8

<웹 개편>
[디자인 컨셉 정하기] 2012/09/20 1w @홍길동 -> [디자인]
[디자인] -> [개발]
    [레이아웃 디자인] 2012/10/01 10h @이수일 # 추가 담당자 확인 필요
    [버튼 디자인] 2012/10/03 20h @심순애

# 개발전 SDK 버전업 검토 필요
[개발]
    [HTML 코딩] 2012/10/07 20h @성춘향
    [스크립트 개발] 2012/10/10 30h @이몽룡
</pre>

