from gendiff import generate_diff


tgt_diff = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_generate_diff():
    first_file = "tests/fixtures/file1.json"
    second_file = "tests/fixtures/file2.json"
    diff = generate_diff(first_file, second_file)
    assert diff == tgt_diff
