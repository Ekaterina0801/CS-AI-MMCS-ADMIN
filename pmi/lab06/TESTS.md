# Тесты · ПМИ · Лабораторная 06

Ровно то, что заведено в сервисе проверки. **Скрытые тесты студенты не видят.**

11 вызовов функций из `solution.py` на 7 баллов. Разбор путей строками: обход каталога в задании уже сделан, функции получают готовый список.

| Вызов | Видимость | Ожидаемое значение |
|---|---|---|
| `count_by_extension(["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"])` | открытый | `{"pdf": 1, "txt": 1, "png": 1, "": 1}` |
| `count_by_extension([])` | открытый | `{}` |
| `count_by_extension(["archive.tar.gz", ".gitignore"])` | 🔒 **скрытый** | `{"gz": 1, "": 1}` |
| `deepest_path(["docs/report.pdf", "notes.txt", "docs/img/logo.png"])` | открытый | `"docs/img/logo.png"` |
| `deepest_path(["a/b/c.txt", "x/y/z.txt"])` | открытый | `"a/b/c.txt"` |
| `deepest_path([])` | 🔒 **скрытый** | `""` |
| `human_size(900)` | открытый | `"900 Б"` |
| `human_size(1536)` | открытый | `"1.5 КБ"` |
| `human_size(5242880)` | открытый | `"5.0 МБ"` |
| `human_size(0)` | 🔒 **скрытый** | `"0 Б"` |
| `human_size(3221225472)` | 🔒 **скрытый** | `"3.0 ГБ"` |
