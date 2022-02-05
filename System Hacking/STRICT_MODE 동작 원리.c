static const int mode1_syscalls[] = {
    __NR_seccomp_read,
    __NR_seccomp_write,
    __NR_seccomp_exit,
    __NR_seccomp_sigreturn,
    -1, /* negative terminated */
};
#ifdef CONFIG_COMPAT
static int mode1_syscalls_32[] = {
    __NR_seccomp_read_32,
    __NR_seccomp_write_32,
    __NR_seccomp_exit_32,
    __NR_seccomp_sigreturn_32,
    0, /* null terminated */
};
#endif
static void __secure_computing_strict(int this_syscall) {
    const int* allowed_syscalls = mode1_syscalls;
#ifdef CONFIG_COMPAT
    if (in_compat_syscall()) allowed_syscalls = get_compat_mode1_syscalls();
#endif
    do {
        if (*allowed_syscalls == this_syscall) return;
    } while (*++allowed_syscalls != -1);
#ifdef SECCOMP_DEBUG
    dump_stack();
#endif
    seccomp_log(this_syscall, SIGKILL, SECCOMP_RET_KILL_THREAD, true);
    do_exit(SIGKILL);
}