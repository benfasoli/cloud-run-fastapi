"""
Example APIRouter that is included in ..main
"""

from fastapi import APIRouter

router = APIRouter()


@router.get('/example',
            summary='Example router endpoint')
def example():
    """Returns hello world"""
    return {'Hello': 'world!'}
