"""empty message

Revision ID: 69c79e79783a
Revises: 6be9b13a5a24
Create Date: 2022-05-20 15:11:52.988346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69c79e79783a'
down_revision = '6be9b13a5a24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cameras',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('camera_type', sa.String(length=200), nullable=False),
    sa.Column('ip_addr', sa.String(length=200), nullable=False),
    sa.Column('rstp_port', sa.Integer(), nullable=False),
    sa.Column('camera_status', sa.Integer(), nullable=False),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ip_addr')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cameras')
    # ### end Alembic commands ###
