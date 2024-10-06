# QEMU on x86_64 (amd64)

Simple qemu call to run VM can look like:
$qemu-system-x86_64 -kernel bzImage -hda rootfs.ext2 -append "root=/dev/sda rw console=ttyS0" --enable-kvm --nographic

-kernel is a compressed kernel image -> can be omitted if complete image is executed (like .img or qemu specific .qcow2) [1]
-hda is for root filesystem -> can be omitted is initramfs is specified (state before fully system load)
-drive file=my-distr.img,index=0,media=disk,format=raw can be used instead, it is fixing qemu warining about unknow format loading
-append "root=/dev/sda rw console=ttyS0" this will be appended to kernel arguments
--enable-kvm is for turning kvm hardware support, the virtualization will be a lot faster
--nographic qemu will run in text mode only

Other example:
$qemu-system-x86_64 -kernel /home/mswiatko/kernels/linux/arch/x86/boot/bzImage -drive file=my-distr.img,index=0,media=disk,format=raw -append "root=/dev/sda" --enable-kvm -m 1G
-m 1G increase the memory for the system to 1G
-drive is used instead of -hda

# buildroot for qemu

The simplest way to build and run system for qemu using buildroot is to use ready for KVM configuration:
$make qemu_x86_64_defconfig
$make j4

In the output/images ther will be start-qemu.sh, simple run it to create VM with these images.

Also the qemu can be run manually:
$qemu-system-x86_64 -kernel bzImage -hda rootfs.ext2 -append "root=/dev/sda rw console=ttyS0" --enable-kvm --nographic

There are some problems with running this filesystem without --nographic option (the idea: lack of graphic support in system built by buildroot, check it!)

# Buildroot and custom kernel

Point -kernel to built kernel compressed image (from arch/x86/boot/bzImage) and run it with exsisting root filesystem (there can be a problem with lack of newest linux headers, but it is fully bootable)
$qemu-system-x86_64 -kernel /home/mswiatko/kernels/linux/arch/x86/boot/bzImage -hda rootfs.ext2 -append "root=/dev/sda rw console=ttyS0" --enable-kvm --nographic

# debootstrap

It is a tool to create file system from exsisting system based on debina/ubuntu releases. It will add whole tools to the builded filesystem.

First we need image to store new filesystem:
$qemu-img create my-distr.img 10G
Creating image with not enough amount of space can lead to the problem in kernel_init during bootting.

Format it:
$mkfs.ext2 my-distr.img

Create folder to mount:
$kmidr mount-point.dir

Mount new image:
$mount -o loop my-distr.img mount-point.dir

Call debootstrap:
$debootstrap --arch=amd64 jammy mount-point.dir http://archive.ubuntu.com/ubuntu/
Architecture and release name (jammy) should match sth in the archive

Umount:
$umount mount-point.dir

Root filesystem is ready and can be booted in qemu:
$qemu-system-x86_64 -kernel /home/mswiatko/kernels/linux/arch/x86/boot/bzImage -drive file=my-distr.img,index=0,media=disk,format=raw -append "root=/dev/sda" --enable-kvm -m 1G

As debootstrap is creating root account without password than can be a problem to login into it (for example on Ubunut, probably because of security reasones).
Created root filesystem can be chroot from host system to make needed changes:

Mount image:
$mount -o loop my-distr.img mount-point.dir

Mount all needed folders:
$mount --make-rslave --rbind /proc mount-point.dir/proc
$mount --make-rslave --rbind /sys mount-point.dir/sys
$mount --make-rslave --rbind /dev mount-point.dir/dev
$mount --make-rslave --rbind /run mount-point.dir/run

Chroot into it:
$chroot mount-point.dir /bin/bash

Change password:
$passwd root

Exit chroot:
$exit

Umount everything:
$umount -R mount-point.dir

There can be a lot more done in chroot on filesystem (ex. installing additional tools, setting network, copying kernel headers etc.)

# Building kernel with debug symbols

$make menuconfig
or
$make kvm_guest.config

Search for CONFIG_DEBUG_INFO and turn it "yes", also FRAME_POINTER can be useful. /* append configuration when it will be found */

Search for x2apic and turn it on to allow qemu to halt timers irq when in breakpoint.

Append -s into qemu, nokaslr for kernel booting arguments, -S is useful as it force qemu to wait for gdb connection.

$qemu-system-x86_64 -kernel /home/mswiatko/kernels/linux/arch/x86/boot/bzImage -drive file=my-distr.img,index=0,media=disk,format=raw -append "root=/dev/sda rw nokaslr" --enable-kvm -m 1G -s

GDB should be connected to the 1234 port (default value). Loading vmlinux needs specific line in ~/.config/gdb/gdbinit:
add-auto-load-safe-path /home/mswiatko/kernels/linux/scripts/gdb/vmlinux-gdb.py
There will be full info about what to do in case vmlinux can't be loaded.

$gdb vmlinux 
$>target remote :1234

## Debug kernel option

Og optimization level had been in kernel, but was removed due to compilation problems and other issues. [1]
In short it is located in Makefile:

(O1 also isn't working on build step) -> probably both can be fixed on x86 by fixing / changing code; however it does not look like good idea

[1] https://lore.kernel.org/lkml/1525566016-30172-5-git-send-email-changbin.du@intel.com/

# QEMU monitor

Monitor directly in QEMU:
$qemu-system-x86_64 -kernel /home/mswiatko/kernels/linux/arch/x86/boot/bzImage -drive file=my-distr.img,index=0,media=disk,format=raw -append "root=/dev/sda rw nokaslr" --enable-kvm -m 1G -s -monitor stdio

Monitor connected via telnet:
$qemu-system-x86_64 -kernel /home/mswiatko/kernels/linux/arch/x86/boot/bzImage -drive file=my-distr.img,index=0,media=disk,format=raw -append "root=/dev/sda rw nokaslr" --enable-kvm -m 1G -s -monitor telnet:127.0.0.1:5555,server,nowait

Telnet connection:
$telnet localhost 5555

Using monitor user can pause, stop, exit VM, and also get useful information using info command.

# QEMU ssh

$qemu-system-x86_64 -kernel /home/mswiatko/kernels/linux/arch/x86/boot/bzImage -drive file=ubuntu-jammy.img,index=0,media=disk,format=raw -append "root=/dev/sda rw nokaslr" --enable-kvm -m 1G -device virtio-net-pci,netdev=mynet -netdev user,id=mynet,hostfwd=tcp::2222-:22 -monitor stdio

The command is forwarding localhost 2222 to 22. It allows ssh connection. Side note, it can be incomplete as it needs to assign ip address on created device on QEMU site:

$ip a a dev enp0s3 10.0.2.15/24
$ip l s dev enp0s3 up

The ip addess can be obtained from QEMU monitor:
$>info usernet

Network manager can be set to assign correct ip address (there is no DHCP in -netdev user mode).

Booted filesystem needs to be prepared for ssh connection. It can be done in chroot (filesystem on Ubunt):
$apt install openssh-server
$vim /etc/ssh/sshd_config
---
PermitRootLogin yes
---

# Debugging using QEMU and GDB

Run QEMU in debug mode (-s):
$qemu-system-x86_64 -kernel /home/mswiatko/kernels/linux/arch/x86/boot/bzImage -drive file=ubuntu-jammy.img,index=0,media=disk,format=raw -append "root=/dev/sda rw nokaslr" --enable-kvm -m 1G -device virtio-net-pci,netdev=mynet -netdev user,id=mynet,hostfwd=tcp::2222-:22 -monitor stdio
-S can be specified to stop QEMU and wait for debugger to attach. It is helpful when debugging startup.

Run GDB with kernel symbols:
$gdb vmlinux 
$>target remote :1234
$b func -> adding breakpoint in function
$b file.c:123 -> adding breakpoint at line
$delete breakpoints -> remove all brekpoints
$add-symobol-file driver.ko address_in_hex -> load symbol of module, the address can be obtained from cat /proc/modules
$lay next -> show being debugged file, next call will show disassembly (also $layout asm)

Remember to call add-symbol-file with correct address_in_hex each time module is reloaded. Even if the address is still the same.

Rest of useful commands in GDB notes.
