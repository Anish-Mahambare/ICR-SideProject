(() => {
  const terms = document.getElementsByClassName('SetPageTerms-term');
  const csv = [];

  Array.from(terms).forEach((term) => {
    const termTexts = term.querySelectorAll('.TermText');
    const word = termTexts[0].textContent.replace(/[\n\r]+/g, '/');
    const def = termTexts[1].textContent.replace(/[\n\r]+/g, '/');
    
    csv.push(`"${word}","${def}"`);
  });

  console.log(csv.join('\n'));
})();
