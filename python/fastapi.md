В фастапи важна последовательность функций. Если я напишу функцию условно 

```python
@app.get('/blog/all')
def all_blog():
    return {'message': 'all blogs'}
```
после вот этой:
```python
@app.get('/blog/{id})
def all_blog(id: int)
    return {'message': f'all blogs {id}'}
```

то первая функция сработает нормально, однако если сделать наоборот, то валидироваться ничего не будет в таком случае

### Tag[s]

```python
from typing import Optional #не забываем


@app.get('/blog/all', tags=['blog'])
def get_all_blogs(page, page_size: Optional[int] = None):
	return {'message': f'this is a size {page_size} of {page}'}
```
теги нужны для того чтобы в Swagger (localhost/docs) как-то отсортировать всю эту хтонь.