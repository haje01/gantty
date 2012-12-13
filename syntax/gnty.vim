" Vim syntax file
" Language: Gantty
" Maintainer: haje01
" Latest Revision: 26 December 2012
if exists("b:current_syntax")
    finish
endif
let b:current_syntax = "gnty"
hi def link taskName    Type
hi def link taskNameRef Identifier
hi def link taskStart   Number
hi def link taskDue     Statement
hi def link taskDone    PreProc
hi def link taskOwner   SpecialChar
hi def link gntyTodo    Todo
hi def link subjectName Special
hi def link gntyComment Comment
hi def link taskDep     Comment
hi def link milestone   Search
syn keyword gntyTodo contained YEAR TODO FIXME NOTE
syn match taskStart contained '\d\{4}\/\d\{2}\/\d\{2}'
syn match taskStart contained '\d\{2}\/\d\{2}'
syn match taskDue contained '\d\+h'
syn match taskDue contained '\d\+d'
syn match taskDue contained '\d\+w'
syn match taskDone contained '\d\+%'
syn match taskOwner contained '@\S*'
syn match gntyComment contained "#.*\$" contains=gntyTodo
syn match gntyComment "#.*" contains=gntyTodo
syn match taskDep contained "->" nextgroup=taskNameRef skipwhite
syn region subjectName start='<' end='>'
syn region taskNameRef start='\[' end='\]' nextgroup=taskNameRef skipwhite
syn region taskNameRef start='\*' end='\*' nextgroup=taskNameRef skipwhite
syn region taskName start='\[' end='\]' nextgroup=taskContent skipwhite
syn region milestone start='\*' end='\*' nextgroup=taskContent skipwhite
syn region taskContent contained start=' ' end='$' contains=taskStart,taskDue,taskDone,taskOwner,taskDep,taskDep,gntyComment
