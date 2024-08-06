"""Initial migration.

Revision ID: fe3a702d7b51
Revises: 19a6dfe6e0be
Create Date: 2024-08-06 13:09:00.516804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe3a702d7b51'
down_revision = '19a6dfe6e0be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('food',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('dish', sa.String(length=100), nullable=False),
    sa.Column('ingredients', sa.Text(), nullable=False),
    sa.Column('grams', sa.Float(), nullable=False),
    sa.Column('calories', sa.Float(), nullable=False),
    sa.Column('dish_calories', sa.Float(), nullable=False),
    sa.Column('meal', sa.String(length=100), nullable=False),
    sa.Column('portion', sa.Float(), nullable=False),
    sa.Column('portion_calories', sa.Float(), nullable=False),
    sa.Column('daily_calories_consumed', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('food')
    # ### end Alembic commands ###
