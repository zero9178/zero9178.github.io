# Projects

This page contains a list of personal projects that I am currently working on or have worked on in the past in order of 
importance.

## [Pylir - An Optimizing Ahead-of-Time Python compiler](https://github.com/zero9178/Pylir)
(May 2021 - ongoing)

The goal of Pylir is to compile and optimize Python code to self-contained native executables while retaining high 
language conformance.
The project heavily relies on MLIR, utilizing it to create custom Python-level IRs and optimisations before lowering it 
to LLVM IR.
Optimisations currently performed include DCE, SCCP, Inlining, SROA, Monomorphization, Redundant Load Elimination,
CSE and more.
Uses LLVMs GC support for an accurate GC and Itanium exception handling for Python exceptions.

Things I am learning in this project include state-of-the-art compiler optimisations, designing a custom fit IR for 
your input language, optimising high-level language aspects not found in e.g. C++, and MLIR.

## [JLLVM - A JVM using LLVM as a JIT](https://github.com/JLLVM/JLLVM)
(Mar. 2023 - ongoing)

```{image} https://github.com/JLLVM/JLLVM/raw/main/logo.png
:width: 20%
:align: center
:alt: Logo of the JLLVM project. A coffee cup with the steam ontop looking similar to the LLVM Wyvern
```

This project is an implementation of a Java 17 compliant JVM.
It uses LLVM as a JIT and compiles JVM bytecode to LLVM IR to produce fast machine-code.
Compilation is done on-demand per-method, causing compilation only on the very first call to a method.
To execute more complicated Java programs, it is capable of using the OpenJDK 17 class library, implementing enough
native methods to run system initialization and a simple "Hello World!".
For memory management, a semi-space copying garbage collector has been implemented which compacts objects on the heap
by relocating them into a different heap space each garbage collection.

This project was part of the course work for the [abstract machines](http://www.complang.tuwien.ac.at/andi/185.966.html)
course at my university.
The project has been implemented together with two friends of mine.

Things I learned in this project included setting up a project for collaboration, using OrcJIT from LLVM, implementing
a relocating garbage collector and JVM internals.

My plan is for this project to also be a learning opportunity for other VM related techniques such as 
tiered-compilation, on-stack replacement, deoptimization, speculative optimizations, fast interpreter implementations
and more.

## [cld - A C99 Compiler Frontend for LLVM](https://github.com/zero9178/cld)
(Feb. 2019 - Oct. 2020)

This project implements a standard conforming compiler capable of compiling C99 programs to object files.
The whole frontend is implemented from scratch and lowers the AST to LLVM IR as a final step.
This is analogous to Clang.
Additionally, it implements many GNU extensions required for the consumption of glibc headers, making it also capable 
to compile and run real world projects such as sqlite or zlib.

This project was my very first compiler and originated in the desire for making a CPU compiler for OpenCL with a focus 
on debugging.
Through this project I ended up learning about lexer and parser theory, semantic analysis, how to write a compiler 
frontend in general, the darkest corners of C and most importantly, how to use LLVM.

## [Micro16C - An optimizing C subset compiler for the Micro16](https://github.com/zero9178/Micro16C)
(Dec. 2020 - Feb. 2021)

The second compiler I wrote and my first time using F#.

This project started as procrastinating studying for my basics of computers course at University.
In that course, a very basic 16-bit CPU, called the [Micro16](https://vowi.fsinf.at/wiki/TU_Wien:Technische_Grundlagen_der_Informatik_VU_(Kastner)/Kapitel_Micro16), 
is introduced as a theoretical construct for students.

This compiler is a compiler for a small subset of C to Micro16 assembly.
The C subset is mostly restricted to what is easily implementable on the CPU.

An input program for Euclid's algorithm may look like: 
```c
int r0 = R0;
int r1 = R1;
int mod;
do
{
    mod = r1 % r0;
    r1 = r0;
    r0 = mod;
}
while(mod != 0);
R2 = r1;
```
and compile to
```
R2 <- R1
R1 <- R0
R0 <- R2
:doWhileBody
(R0); if N goto .modNeg
goto .cont
:modNeg
R0 <- ~R0
R0 <- 1 + R0
:cont
R2 <- ~R1
R2 <- 1 + R2
:modBody
R3 <- R2 + R0; if N goto .modEnd
R0 <- R3; goto .modBody
:modEnd
(R0); if Z goto .doWhileContinue
R2 <- R1
R1 <- R0
R0 <- R2; goto .doWhileBody
:doWhileContinue
R2 <- R1
```

This project was my first time writing an optimizing compiler and a CPU backend.
Things I learned included SSA construction, dataflow analysis, SCCP, jump threading, peephole optimizations, 
instruction selection and register allocation, both linear register allocation in the first iteration, followed by 
register allocation via graph colouring in a second implementation.

## [Scientific Calculator in Minecraft](https://github.com/zero9178/Minecraft-Scientific-Calculator)
(2017)

```{figure} https://raw.githubusercontent.com/zero9178/Minecraft-Scientific-Calculator/master/Calculator.png
---
align: center
---
Sideview of the calculator
```

This project is a fully fledged CPU built using just Redstone in Minecraft.
It consists an 8-bit ALU for integer operations, an IEEE 754 Half-precision floating point FPU and a 4kB ROM 
containing the calculator program.
The FPU is capable of performing the four basic math operations, square root and smaller miscellaneous functions like 
absolute.
Using a custom ISA, a calculator program was written which contains the implementations of more complex functions such
as sine, cosine, exponential function and logarithm. These are implemented using taylor series'.

This project was the last project that I did prior to getting into programming.