#  Mini Compiler IF-ELSE

 Deskripsi

Mini Compiler IF-ELSE merupakan program sederhana yang dibuat menggunakan Python untuk mensimulasikan tahapan utama dalam proses kompilasi. Program ini mengimplementasikan empat tahap utama compiler, yaitu:

- Analisis Leksikal (Lexical Analysis)
- Analisis Sintaksis (Syntax Analysis)
- Analisis Semantik (Semantic Analysis)
- Generasi Kode Antara (Three-Address Code / TAC)

Konstruksi sintaksis yang dipilih pada implementasi ini adalah **percabangan IF-ELSE**.

# Mahasiswa
* **Nama:** M. Akbar khadafi.A
* **NIM:** 231011401717
* **kelas:** 06TPLM002

---

# Grammar (BNF)

```bnf
<if_stmt> ::= if ( <condition> ) { <statement> } else { <statement> }

<condition> ::= <identifier> <operator> <identifier>

<statement> ::= <identifier> = <identifier> ;

<identifier> ::= letter { letter | digit }

<operator> ::= > | < | == | != | >= | <=
```

---

Cara Menjalankan Program

Pastikan Python sudah terpasang.

Clone repository:

```bash
git clone https://github.com/soeharto2/MiniCompiler.git
```

Masuk ke folder project:

```bash
cd MiniCompiler
```

Jalankan program:

```bash
python compiler.py
```

---

# Contoh Input

```c
if(a>b){c=a;}else{c=b;}
```

---

# Tahapan Kompilasi

## 1. Analisis Leksikal

Tahap ini bertugas memecah source code menjadi token-token yang dapat dipahami oleh compiler.

Contoh token yang dihasilkan:

```text
IF           : if
LPAREN       : (
IDENTIFIER   : a
OPERATOR     : >
IDENTIFIER   : b
RPAREN       : )
LBRACE       : {
IDENTIFIER   : c
ASSIGN       : =
IDENTIFIER   : a
SEMICOLON    : ;
RBRACE       : }
ELSE         : else
```

---

## 2. Analisis Sintaksis (AST)

Pada tahap ini token yang dihasilkan akan disusun menjadi struktur pohon sederhana (Abstract Syntax Tree).

```text
IF
├── Condition
│   ├── a
│   ├── >
│   └── b
├── THEN
│   └── c = a ;
└── ELSE
    └── c = b ;
```

---

## 3. Analisis Semantik

Tahap ini melakukan pengecekan apakah seluruh variabel telah dideklarasikan.

Jika benar:

```text
Semantic Check : SUCCESS
```

Jika terdapat variabel yang belum dideklarasikan:

```text
Semantic Error : Variabel 'x' belum dideklarasikan.
```

---

## 4. Three Address Code (TAC)

AST kemudian diterjemahkan menjadi kode antara (Three-Address Code).

```text
if a > b goto L1
goto L2

L1:
c = a
goto L3

L2:
c = b

L3:
END
```

---

# Contoh Output Program

```text
==================================================
      MINI COMPILER - IF ELSE
==================================================

===== LEXICAL ANALYSIS =====
IF           : if
LPAREN       : (
IDENTIFIER   : a
OPERATOR     : >
IDENTIFIER   : b
RPAREN       : )
LBRACE       : {
IDENTIFIER   : c
ASSIGN       : =
IDENTIFIER   : a
SEMICOLON    : ;
RBRACE       : }
ELSE         : else
LBRACE       : {
IDENTIFIER   : c
ASSIGN       : =
IDENTIFIER   : b
SEMICOLON    : ;
RBRACE       : }

===== SYNTAX ANALYSIS =====
IF
├── Condition
│   ├── a
│   ├── >
│   └── b
├── THEN
│   └── c = a ;
└── ELSE
    └── c = b ;

===== SEMANTIC ANALYSIS =====
Semantic Check : SUCCESS

===== THREE ADDRESS CODE =====
if a > b goto L1
goto L2

L1:
c = a
goto L3

L2:
c = b

L3:
END
```

---

Teknologi yang Digunakan

- Python 3
- Regular Expression (Regex)
- Visual Studio Code

---

#  Kesimpulan

Program Mini Compiler IF-ELSE berhasil mensimulasikan tahapan utama dalam proses kompilasi, mulai dari analisis leksikal, sintaksis, semantik, hingga menghasilkan Three-Address Code (TAC). Implementasi ini memberikan gambaran sederhana mengenai cara kerja sebuah compiler dalam memproses kode sumber sebelum diterjemahkan menjadi representasi yang lebih rendah.
