from src.core.entities.postdto import PostDto
from src.domain.parsers.far_post.entities import ListPagePost, DetailPagePost
from src.domain.post.model import PostModel


class PostMapper:

    @staticmethod
    def from_parser_page_obj_to_post(list_page_obj: ListPagePost, detail_page_obj: DetailPagePost) -> PostDto:
        return PostDto(
            id=list_page_obj.id,
            title=list_page_obj.title,
            author=detail_page_obj.author,
            views_number=list_page_obj.views_number,
            index=list_page_obj.index
        )

    @staticmethod
    def from_post_model_to_post_dto(post_model: PostModel) -> PostDto:
        return PostDto(
            id=post_model.id,
            title=post_model.title,
            author=post_model.author,
            views_number=post_model.views_number,
            index=post_model.index
        )
