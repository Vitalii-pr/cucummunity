"""“commentLike_and_date_to_post_and_comments”

Revision ID: 44b7bf1d4891
Revises: 7e285ab5fe34
Create Date: 2024-03-13 01:00:55.358931

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44b7bf1d4891'
down_revision: Union[str, None] = '7e285ab5fe34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Following', sa.Column('follower_id', sa.Integer(), nullable=False))
    op.alter_column('Following', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_foreign_key(None, 'Following', 'Users', ['follower_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Following', type_='foreignkey')
    op.alter_column('Following', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('Following', 'follower_id')
    # ### end Alembic commands ###