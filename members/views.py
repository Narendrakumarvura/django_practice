from django.shortcuts import render, get_object_or_404,redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages
from .utils import send_welcome_email
#list members
def member_list(request):
    members=Member.objects.all()
    return render(request,'members/member_list.html',{'members':members})

#members Details
def member_detail(request, pk):
    member=get_object_or_404(Member, pk=pk)
    return render (request, 'members/member_detail.html',{'member':member})

#create member
def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            # Use first_name and last_name instead of name
            full_name = f"{member.first_name} {member.last_name}"
            if send_welcome_email(member.email, full_name):
                messages.success(request, "Member created and email sent successfully.")
            else:
                messages.warning(request, "Member created, but email could not be sent.")
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'members/member_form.html', {'form': form})

#update member
def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_detail', pk=member.pk)  # Use pk here for redirection
    else:
        form = MemberForm(instance=member)

    return render(request, 'members/member_form.html', {'form': form})


#delete member
def member_delete(request, pk):
    member=get_object_or_404(Member,pk=pk)
    if request.method=='POST':
        member.delete()
        return redirect('member_list')
    return render(request,'members/member_confirm_delete.html',{'member':member})

