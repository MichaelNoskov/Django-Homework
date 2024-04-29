from django.core.exceptions import ValidationError
from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _


STATUS = [
    'in progress',
    'completed',
    'cancelled',
    'created'
]
POSITIONS = [
    'director',
    'junior developer',
    'middle developer',
    'senior developer',
    'hr specialist'
]


def check_status_exists(status) -> None:
    if status not in STATUS:
        raise ValidationError(
            f'status should be in list: {", ".join(STATUS)}',
        )


def check_position_exists(position) -> None:
    if position not in POSITIONS:
        raise ValidationError(
            f'status should be in list: {", ".join(POSITIONS)}',
        )


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, blank=True, editable=False, default=uuid4)

    class Meta:
        abstract = True


class Task(UUIDMixin):
    name = models.TextField(_('name'), null=False, blank=False)
    description = models.TextField(_('description'), null=False, blank=False)
    status = models.TextField(_('status'), null=False, blank=False, validators=[check_status_exists])
    developers = models.ManyToManyField('Developer', verbose_name=_('developers'), through='TaskDeveloper')

    def __str__(self) -> str:
        return f'"{self.name}": {self.status}'

    class Meta:
        db_table = '"freelance"."task"'
        ordering = ['name', 'status']
        verbose_name = _('task')
        verbose_name_plural = _('tasks')


class Developer(UUIDMixin):
    firstname = models.TextField(_('firstname'), null=False, blank=False)
    surname = models.TextField(_('surname'), null=False, blank=False)
    position = models.TextField(_('position'), null=False, blank=False, validators=[check_position_exists])
    tasks = models.ManyToManyField('Task', verbose_name=_('tasks'), through='TaskDeveloper')

    def __str__(self) -> str:
        return f'{self.surname} {self.firstname} ({str(self.position)})'

    class Meta:
        db_table = '"freelance"."developer"'
        ordering = ['surname', 'firstname']
        verbose_name = _('developer')
        verbose_name_plural = _('developers')


class Comment(UUIDMixin):
    content = models.TextField(_('content'), null=False, blank=False)
    publication_date = models.DateField(_('publication date'), null=False, blank=False)
    task = models.ForeignKey('Task', verbose_name=_('task'), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.content} - {self.publication_date}'

    class Meta:
        db_table = '"freelance"."comment"'
        ordering = ['content']
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class TaskDeveloper(models.Model):
    developer = models.ForeignKey('Developer', verbose_name=_('developer'),  on_delete=models.CASCADE)
    task = models.ForeignKey(Task, verbose_name=_('task'), on_delete=models.CASCADE)

    class Meta:
        db_table = '"freelance"."task_developer"'
        unique_together = (
            ('task', 'developer'),
        )
        verbose_name = _('relationship task developer')
        verbose_name_plural = _('relationships task developer')
