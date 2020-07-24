"""news

Revision ID: 539657e48fd1
Revises: 0ad1f7bca26b
Create Date: 2020-03-02 12:31:50.050149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '539657e48fd1'
down_revision = '0ad1f7bca26b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
        sa.Column('id', sa.Integer, nullable=False, autoincrement=True),
        sa.Column('outlet', sa.String(length=140), nullable=True),
        sa.Column('category', sa.String(length=140), nullable=True),
        sa.Column('title', sa.String(length=140), nullable=False),
        sa.Column('link', sa.String(length=140), nullable=True),
        sa.Column('summary', sa.String(length=140), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    # ### end Alembic commands ###