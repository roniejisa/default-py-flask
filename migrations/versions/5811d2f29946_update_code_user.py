"""update code user

Revision ID: 5811d2f29946
Revises: 1b01c88f4fba
Create Date: 2024-09-27 10:56:19.096809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5811d2f29946'
down_revision = '1b01c88f4fba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('firstname', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('lastname', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('password', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('password')
        batch_op.drop_column('lastname')
        batch_op.drop_column('firstname')

    # ### end Alembic commands ###
