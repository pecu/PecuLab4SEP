import React from "react";

export function OpenBlind({ openblind }) {
  return (
    <div>
      <h4>OpenBlind</h4>
      <form
        onSubmit={(event) => {
          // This function just calls the transferTokens callback with the
          // form's data.
          event.preventDefault();

          const formData = new FormData(event.target);
          const opened = formData.get("opened");
          console.log(opened);
          const nft_id = formData.get("nft_id");
          console.log(nft_id);
          openblind(opened, nft_id);
        }}
      >
        <div className="form-group">
          <label>Open Blind Box</label>
          <select name="opened" required>
            <option value={1}>true</option>
            <option value={0}>false</option>
          </select>
          <input className="form-control" type="text" name="nft_id" required />
        </div>
        <div className="form-group">
          <input className="btn btn-primary" type="submit" value="setBox" />
        </div>
      </form>
    </div>
  );
}
