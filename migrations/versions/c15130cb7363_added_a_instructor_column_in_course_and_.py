"""added a instructor column in course and dropped the access column

Revision ID: c15130cb7363
Revises: d0e10d07527d
Create Date: 2019-10-29 13:22:28.114149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c15130cb7363'
down_revision = 'd0e10d07527d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('instructor', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'course', ['instructor'])
    op.drop_column('user', 'access')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('access', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'course', type_='unique')
    op.drop_column('course', 'instructor')
    # ### end Alembic commands ###
