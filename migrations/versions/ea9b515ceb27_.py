"""empty message

Revision ID: ea9b515ceb27
Revises: 
Create Date: 2022-05-20 09:49:42.957994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea9b515ceb27'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cameras',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('camrea_type', sa.String(length=200), nullable=False),
    sa.Column('ip_add', sa.String(length=200), nullable=False),
    sa.Column('camrea_status', sa.Integer(), nullable=False),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cameras')
    # ### end Alembic commands ###