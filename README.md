# gantty - 간트챠트를 위한 컴팩트 신택스

자신이 사용하는 텍스트 에디터로 누구나 쉽게 간트챠트를 작성하자!

## 테스크
테스크는의 단위를 말한다.
테스크는 다음과 같이 `[` `]`안에 이름을 기술한다.

<pre>
[디자인]
</pre>

## 시작일
시작일은 테스크가 시작하는 날짜를 의미한다.
시작일은 테스크 이름 뒤에 다음과 같이 년/월/일 형식으로 기술한다.

<pre>
[디자인] 2012/10/01
</pre>

##시간
작업시간은 테스크를 끝내기 위해 필요한 시간이다. 
작업시간은 시간(h) 일(d) 주(w) 단위로 표기할 수 있다. 
예를 들어 30시간이 필요한 경우 다음과 같이 기술한다.

<pre>
[디자인] 2012/10/01 30h
</pre>

*서로 다른 단위를 섞어서 사용하지는 못한다.*

##작업자
실제을 할 사람을 말한다.
작업자는 다음과 같이 `@` + 이름 형식으로 기술 한다.

<pre>
[디자인] 2012/10/01 30h @김정주
</pre>

한명 이상인 경우 이어서 기술한다.

<pre>
[디자인] 2012/10/01 30h @김정주 @박현우
</pre>

## 하위작업
특정이 세부으로 나누어지는 경우, 다음과 같이 하위으로 기술한다.

<pre>
[디자인]
    [레이아웃 디자인] 2012/10/01 10h @김정주
    [버튼 디자인] 2012/10/03 20h @박현우
</pre>

하위작업이 있는 경우 상위작업에는 따로 시작일,시간,자 같은 정보를 기술하지 않는다.


## 의존작업
어떤을 시작하기위해 먼저 수행되어야할을 말한다.
의존은 다음과 같이 `->`로 기술한다.

<pre>
[디자인 컨셉 정하기] 2012/09/20 100h @홍길동 -> [디자인]
[디자인]
    [레이아웃 디자인] 2012/10/01 10h @김정주
    [버튼 디자인] 2012/10/03 20h @박현우
</pre>

위의 예는 '버튼을 디자인하기 위해서 먼저 디자인 컨셉을 정해야 한다'는 뜻이 된다.

## 서브젝트

서브젝트는 장기 목표를 위해 사용된다. 서브젝트에 하나 이상의 테스크가 등록된다.
서브젝트는 다음과 같이 `<` `>` 안에 이름을 기술한다.

<pre>
<웹 개편>
[디자인 컨셉 정하기] 2012/09/20 100h @홍길동 -> [디자인]
[디자인] -> [개발]
    [레이아웃 디자인] 2012/10/01 10h @김정주
    [버튼 디자인] 2012/10/03 20h @박현우
[개발]
    [HTML 코딩] 2012/10/07 20h @김정주
    [스크립트 개발] 2012/10/10 30h @박현우
</pre>

