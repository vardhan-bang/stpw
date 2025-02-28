	.file	"test.c"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	$12, -4(%rbp)
	cmpl	$57, -4(%rbp)
	jg	.L2
	movl	$50, -8(%rbp)
	jmp	.L3
.L4:
	addl	$96, -4(%rbp)
	addl	$1, -8(%rbp)
.L3:
	cmpl	$38, -8(%rbp)
	je	.L4
.L2:
	movl	$0, %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Debian 12.2.0-14) 12.2.0"
	.section	.note.GNU-stack,"",@progbits
