"""initial

Revision ID: e624eb9b7f96
Revises: 
Create Date: 2024-12-02 13:31:43.991600

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e624eb9b7f96"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "cats",
        sa.Column("name", sa.String(length=20), nullable=False),
        sa.Column("years_of_exp", sa.Integer(), nullable=False),
        sa.Column("breed", sa.String(), nullable=False),
        sa.Column("salary", sa.Integer(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("cats")
    # ### end Alembic commands ###