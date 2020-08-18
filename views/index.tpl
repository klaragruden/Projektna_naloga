%rebase('base.tpl')
%import model

 
<blockquote>
    <h3'><i>Spomin je najboljša igra za urjenje spomina ;).</i></h3>
</blockquote>

<table>

  
  <tr>
      <td><b>Izberi težavnost:</b></td>
  </tr>
  
  <tr>
      <td>
          <form action="/nova_igra/" method="POST">
              <input type="radio" name="tezavnost" value="1"> Lahko<br>
              <input type="radio" name="tezavnost" value="2"> Srednje<br>
              <input type="radio" name="tezavnost" value="3"> Tezko<br>  
              <p><input type="submit" value="prični igro"></p>
          </form>
      </td>
  </tr>

</table>

    
 
