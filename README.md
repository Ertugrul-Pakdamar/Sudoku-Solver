# Sudoku Solver

Bu Python programı, 9x9'luk bir Sudoku bulmacasını çözmek için geri izleme algoritmasını kullanır.

## İçindekiler

- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Fonksiyonlar](#fonksiyonlar)
- [Katkıda Bulunma](#katkıda-bulunma)
- [İletişim][#iletişim]

## Özellikler

- 9x9'luk Sudoku bulmacasını çözer.
- Geri izleme (backtracking) algoritması kullanır.

## Kurulum

1. **Depoyu klonlayın:**
    ```sh
    git clone https://github.com/kullanici_adi/sudoku-solver.git
    cd sudoku-solver
    ```

2. **Gerekli bağımlılıkları yükleyin:**
    Bu proje sadece Python standard kütüphanelerini kullanır, bu yüzden ekstra bağımlılıklar yoktur.

## Kullanım

1. **Python dosyasını çalıştırın:**
    ```sh
    python sudoku_solver.py
    ```

2. **Örnek Sudoku Tahtası:**
    Kodu çalıştırdığınızda, önceden tanımlanmış bir Sudoku tahtasını çözmek için programı kullanabilirsiniz.

## Fonksiyonlar

- `solve_sudoku(board)`: Sudoku tahtasını çözer.
- `find_empty_cell(board)`: Boş hücreyi bulur.
- `is_valid(board, num, row, col)`: Numaranın belirtilen konuma yerleştirilip yerleştirilemeyeceğini kontrol eder.

## Katkıda Bulunma

1. Depoyu fork edin.
2. Yeni bir dal oluşturun (git checkout -b feature-branch).
3. Değişikliklerinizi commit edin (git commit -m 'Yeni özellik ekle').
4. Dalınıza push edin (git push origin feature-branch).
5. Yeni bir Pull Request oluşturun.

## İletişim

Ertuğrul Pakdamar - [GitHub](https://github.com/Ertugrul-Pakdamar)
