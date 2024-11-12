import pytest
from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(100, 200) == 300

def test_add_type_error():
    with pytest.raises(TypeError):
        add("2", 3)  # 测试不正确类型的输入