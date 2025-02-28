	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 15, 0	sdk_version 15, 2
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	str	wzr, [sp, #12]
	mov	w8, #90                         ; =0x5a
	str	w8, [sp, #8]
	ldr	w8, [sp, #8]
	subs	w8, w8, #61
	cset	w8, ne
	tbnz	w8, #0, LBB0_4
	b	LBB0_1
LBB0_1:
	ldr	w8, [sp, #8]
	subs	w8, w8, #63
	cset	w8, eq
	tbnz	w8, #0, LBB0_3
	b	LBB0_2
LBB0_2:
	ldr	w8, [sp, #8]
	subs	w8, w8, #32
	str	w8, [sp, #8]
	b	LBB0_3
LBB0_3:
	b	LBB0_4
LBB0_4:
	mov	w0, #0                          ; =0x0
	add	sp, sp, #16
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols
