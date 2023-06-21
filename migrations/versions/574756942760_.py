"""empty message

Revision ID: 574756942760
Revises: d1c96509db86
Create Date: 2023-06-21 16:08:02.220302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '574756942760'
down_revision = 'd1c96509db86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('avatar_hash', sa.String(length=32), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('avatar_hash')

    # ### end Alembic commands ###