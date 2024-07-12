(() => {
  const terms = document.getElementsByClassName('SetPageTerms-term');
  const csv = [];

  Array.from(terms).forEach((term) => {
    const termTexts = term.querySelectorAll('.TermText');
    const word = termTexts[0].textContent.replace(/[\n\r]+/g, '/');
    const def = termTexts[1].textContent.replace(/[\n\r]+/g, '/');
    
    csv.push(`"${word}","${def}"`);
  });

  const csvContent = csv.join('\n');

  
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });

  
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = 'terms.csv'; 

  document.body.appendChild(link);


  link.click();


  document.body.removeChild(link);
})();
    
