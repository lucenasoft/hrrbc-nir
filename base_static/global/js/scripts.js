function my_scope() {
    const forms = document.querySelectorAll('.form-delete');
  
    for (const form of forms) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
  
        const confirmed = confirm('Deseja excluir a transferência?');
  
        if (confirmed) {
          form.submit();
        }
      });
    }
  }
  
  my_scope();