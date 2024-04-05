from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from veggie_recipe_book.recipes.models import Recipe, Like, Comment
from veggie_recipe_book.social.forms import CommentForm


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'partials/add_comment.html'

    def form_valid(self, form):
        recipe_id = self.kwargs['recipe_id']
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        form.instance.recipe = recipe
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        recipe_id = self.kwargs['recipe_id']
        return reverse('details_recipe', kwargs={'pk': recipe_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, pk=self.kwargs['recipe_id'])
        return context


@login_required
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    like, created = Like.objects.get_or_create(user=request.user, recipe=recipe)
    return HttpResponseRedirect(reverse('details_recipe', args=[recipe_id]))


@login_required
def unlike_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    like = Like.objects.filter(user=request.user, recipe=recipe)
    like.delete()
    return HttpResponseRedirect(reverse('details_recipe', args=[recipe_id]))
