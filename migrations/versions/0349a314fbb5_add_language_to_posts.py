"""add language to posts

Revision ID: 0349a314fbb5
Revises: 1012706fe0a0
Create Date: 2019-04-11 10:57:38.832441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0349a314fbb5'
down_revision = '1012706fe0a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
